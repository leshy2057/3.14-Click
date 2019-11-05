import os, shutil, sys, time

try:
    print("Trying import cx_Freeze")
    time.sleep(2)
    import cx_Freeze
except:
    print("Failed!")
    print("You don't have cx_Freeze. Do you wan't install? (Y|n)", end=" ")
    if (input().upper() == "Y"):
        os.system("pip install cx_Freeze")
        import cx_Freeze
    else:
        sys.exit()

exe = [cx_Freeze.Executable("PiClick.py", icon="Images\\ava.ico", base = "Win32GUI")] # <-- HERE
build_exe_options = {'build_exe': '3.14 Click'}

cx_Freeze.setup(
    name = "3.14Click",
    version = "1.0",
    options = {"build_exe": build_exe_options},
    executables = exe
)

shutil.move("Images", "3.14 Click\\Images")
shutil.move("Files", "3.14 Click\\Files")
shutil.move("Saves", "3.14 Click\\Saves")
shutil.move("Classes", "3.14 Click\\Classes")
os.remove("PiClick.py")
os.remove("setup.py")