import sys
import os
"""from dotenv import load_dotenv

load_dotenv()  # Load .env file
print("Loading environment variables...")"""

from ..ui.gui import AssistantGUI

def main():
    print("Launching Digital Assistant GUI...")
    AssistantGUI()

if __name__ == "__main__": main()