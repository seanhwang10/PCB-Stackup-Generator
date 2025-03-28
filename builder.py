#!/usr/bin/env python3
import subprocess
import sys

def check_and_install_pyinstaller():
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_exe():
    print("Building executable from filenamer.py...")
    command = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "filenamer.py"
    ]
    try:
        subprocess.check_call(command)
        print("Executable built successfully!")
        print("Check the 'dist' folder for your executable.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while building the executable.")
        sys.exit(1)

if __name__ == "__main__":
    check_and_install_pyinstaller()
    build_exe()
