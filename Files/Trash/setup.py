import cx_Freeze

exe = [cx_Freeze.Executable("main.py", icon = "D:\\GITHUB\\3.14-Click\\Images\\ava.ico", base = "Win32GUI")] # <-- HERE

cx_Freeze.setup(
    name = "3.14Click",
    version = "1.0",
    executables = exe
) 