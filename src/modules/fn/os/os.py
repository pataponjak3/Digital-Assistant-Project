from ....interfaces.functionality import Functionality
import os
import subprocess
from win32com.client import Dispatch
from rapidfuzz import process, fuzz

class OSFunctionality(Functionality):
    # Define common Start Menu directories
    START_MENU_DIRS = [
        os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
        os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs")
    ]

    EXCLUDE_KEYWORDS = ["uninstall", "setup", "remove", "update", "help", "readme", "documentation", "docs", "manual", "config", "configuration", "preferences", "settings", "about", "license", "legal", "terms", "privacy"]
    def get_functions_description(self):
        return [
"""Function: launch_application
Module: os
Description: Launches an application by its name in the system.
Arguments:
- app_name (string): The name of the application to launch.
"""
        ]
    
    """Function: find_file
Module: os
Description: Finds a file by its name in the system.
Arguments:
- file_name (string): The name of the file to find.
"""

    def execute_function(self, name: str, args: dict):
        return getattr(self, f"_{name}")(**args)
    
    def __is_valid_app_shortcut(self, path: str) -> bool:
        ext = os.path.splitext(path)[1].lower()
        if ext not in [".lnk", ".url"]:
            return False

        try:
            shell = Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(path)
            target = shortcut.TargetPath.lower()

            if ext == ".lnk" and not target.endswith(".exe"):
                return False
            if any(kw in target for kw in self.EXCLUDE_KEYWORDS):
                return False
            return True
        except Exception:
            return False
        
    def __get_all_shortcuts(self):
        shortcuts = {}
        for base_dir in self.START_MENU_DIRS:
            for root, _, files in os.walk(base_dir):
                for file in files:
                    ext = os.path.splitext(file)[1].lower()
                    if ext not in [".lnk", ".url"]:
                        continue
                    full_path = os.path.join(root, file)
                    if self.is_valid_shortcut(full_path):
                        name = os.path.splitext(file)[0].strip().lower()
                        shortcuts[name] = full_path
        return shortcuts
    
    def _launch_application(self, app_name: str):
        app_query = app_name.lower().strip()

        existing_dirs = [d for d in self.START_MENU_DIRS if os.path.isdir(d)]
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
        
        matches = process.extract(
            query=app_query,
            choices=shortcuts.keys(),
            scorer=fuzz.token_sort_ratio,
            limit=5
        )

        high_matches = [match for match in matches if match[1] >= 80]

        if not high_matches:
            return (
                f"No matching applications found for '{app_query}'.\n"
                "Make sure the application has a shortcut in the Start Menu and try again."
            )

        if len(high_matches) == 1:
            match_name = high_matches[0][0]
            subprocess.Popen(shortcuts[match_name], shell=True)
            return f"Launched '{match_name.title()}'."
        else:
            options = "\n".join([f"- {match[0].title()} ({match[1]}% match)" for match in high_matches])
            return f"Multiple possible matches found:\n{options}\nPlease specify which one you meant."