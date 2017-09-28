import cx_Freeze
import sys

base = None

executables = [
    cx_Freeze.Executable("interface.py")]
cx_Freeze.setup(
        name="Algorithmen",
        options={
            "build_exe": {
                "packages": [
                "time", "subprocess"],
                "include_files": [
                "ChiSquared.py",
                "ParameterFinden.py",
                "Primzahlen.txt",
                "RandomGenerator.py",
                "RandomSeq.py",
                "SequenzGenerator.py",
            ]}
        },
        version="1",
        description="Algorithmen der Seminararbeit",
        executables=executables
    )

