import os
import subprocess


def clear_console():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)
