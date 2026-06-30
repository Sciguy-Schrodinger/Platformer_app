from pathlib import Path
import sys
import os

def resource_path(filename):
    try:
        # When run from PyInstaller bundle
        base_path = sys._MEIPASS
    except AttributeError:
        # When run from source
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)
