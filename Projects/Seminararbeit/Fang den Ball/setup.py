import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

executables = [
    cx_Freeze.Executable("Main.py")
]
cx_Freeze.setup(
    name="Fang den Ball!",
    options={
        "build_exe": {
            "packages": [
                "pygame",
                "random",
            ], "include_files": [
                "Button.py",
                "Constants.py",
                "Game.py",
            ]
        }
    },
    version="1",
    description="Spiel der Seminararbeit",
    executables=executables
)
