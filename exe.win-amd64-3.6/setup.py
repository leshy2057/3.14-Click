import cx_Freeze

exe = [cx_Freeze.Executable("main.py", base = "Win32GUI")] # <-- HERE

cx_Freeze.setup(
    name = "3.14Click",
    version = "1.0",
    executables = exe
) 