from interfaces.functionality_interface import Functionality
import os
import subprocess
from win32com.client import Dispatch
from rapidfuzz import process, fuzz

class OSFunctionality(Functionality):
    # Define common Start Menu directories
    __START_MENU_DIRS = [
        os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
        os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs")
    ]

    __EXCLUDE_KEYWORDS = ["uninstall", "setup", "remove", "update", "help", "readme", "documentation", "docs", "manual", "config", "configuration", "preferences", "settings", "about", "license", "legal", "terms", "privacy"]

    def get_functions_description(self):
        return [
"""Function: launch_application
Module: os
Description: Launches an application by its name in the system, if it has a shortcut in the Start Menu.
Arguments:
- app_name (string): The name of the application to launch.
- is_sure_after_multiple_matches (bool): Indicates if the user confirmed which application to launch when multiple matches were found before in the conversation.
"""
        ]
    
    """Function: find_file
Module: os
Description: Finds a file by its name in the system.
Arguments:
- file_name (string): The name of the file to find.
"""

    def get_functions_schema(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "os_launch_application",
                    "description": "Launches an application by its name in the system, if it has a shortcut in the Start Menu.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "app_name": {
                                "type": "string",
                                "description": "The name of the application to launch.",
                            },
                            "is_sure_after_multiple_matches": {
                                "type": "boolean",
                                "description": "Indicates if the user confirmed which application to launch when multiple matches were found before in the conversation.",
                                "default": False
                            }
                        },
                        "required": ["app_name", "is_sure_after_multiple_matches"]
                    }
                }
            }
        ]

    def execute_function(self, name: str, args: dict, supports_function_calls: bool):
        return getattr(self, f"_{name}")( **args)
    
    def __is_valid_app_shortcut(self, path: str) -> bool:
        """Validates if the given path is a valid application shortcut.
        
        :param path: The path to the shortcut file.
        :type path: str
        :return: A boolean indicating if the shortcut is valid.
        :rtype: bool
        """
        ext = os.path.splitext(path)[1].lower()
        if ext not in [".lnk", ".url"]:
            return False

        try:
            shell = Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(path)
            target = shortcut.TargetPath.lower()

            if ext == ".lnk" and not target.endswith(".exe"):
                return False
            if any(kw in target for kw in self.__EXCLUDE_KEYWORDS):
                return False
            return True
        except Exception:
            return False
        
    def __get_all_shortcuts(self) -> dict:
        """Recursively retrieves all valid application shortcuts from the Start Menu directories.
        
        :return: A dictionary mapping application names to their shortcut paths.
        :rtype: dict
        """
        shortcuts = {}
        for base_dir in self.__START_MENU_DIRS:
            for root, _, files in os.walk(base_dir):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext not in [".lnk", ".url"]:
                        continue
                    full_path = os.path.join(root, file)
                    if self.__is_valid_app_shortcut(full_path):
                        name = os.path.splitext(file)[0].strip().lower()
                        shortcuts[name] = full_path
        print
        return shortcuts
    
    def __get_best_matches(self, app_name: str, shortcuts: dict, limit=5, score_threshold=80) -> list[tuple[str, int]]:
        """Finds the best matching application shortcuts based on the provided application name.
        
        :param app_name: The name of the application to match.
        :type app_name: str
        :param shortcuts: A dictionary mapping application names to their shortcut paths.
        :type shortcuts: dict
        :param limit: The maximum number of matches to return.
        :type limit: int
        :param score_threshold: The minimum score threshold for a match.
        :type score_threshold: int
        :return: A list of tuples containing the matched application names and their scores.
        :rtype: list[tuple[str, int]]"""
        matches = process.extract(
            query=app_name,
            choices=shortcuts.keys(),
            scorer=fuzz.partial_ratio,
            limit=limit
        )

        return [(match, score) for match, score, _ in matches if score >= score_threshold]
    
    def _launch_application(self, app_name: str, is_sure_after_multiple_matches: bool=False) -> str:
        """Launches an application by its name.
        
        :param app_name: The name of the application to launch.
        :type app_name: str
        :return: A string indicating the result of the launch attempt.
        :rtype: str
        """

        app_query = app_name.lower().strip()
            
        existing_dirs = [d for d in self.__START_MENU_DIRS if os.path.isdir(d)]
        if not existing_dirs:
            return (
                "Start Menu directories could not be found. "
                "This functionality depends on application shortcuts located in the Windows Start Menu. "
                "Make sure you're using a compatible version of Windows and the Start Menu is available."
            )
        
        shortcuts = self.__get_all_shortcuts()
        if not shortcuts:
            return (
                "No application shortcuts were found in the Start Menu.\n"
                "Only applications that have Start Menu shortcuts can be launched by this assistant. "
                "If your desired application is not found, please ensure it has a shortcut in the Start Menu."
            )
        
        high_matches = self.__get_best_matches(app_query, shortcuts)

        if not high_matches:
            return (
                f"No matching applications found for '{app_query}'.\n"
                "Make sure the application has a shortcut in the Start Menu and try again."
            )
        
        try:
            if len(high_matches) == 1 or is_sure_after_multiple_matches:
                match_name = high_matches[0][0]
                subprocess.Popen(shortcuts[match_name], shell=True)
                return f"Launched '{match_name.title()}'."
            else:
                options = "\n".join([f"- [{i+1}]{match[0].title()} ({match[1]}% match)" for i, match in enumerate(high_matches)])
                return f"Multiple possible matches found:\n{options}\n\nPlease specify which one you meant."
        except Exception as e:
            return f"Error launching application: {e}"