import os

os.system("pip install colorama")
os.system("pip install pyautogui")
os.system("pip install pyinstaller")

os.system("pyinstaller --onefile caffeine.py")
os.system("cp dist/caffeine /bin")
cu = os.getcwd()

os.chdir("/etc")
os.mkdir("caffeine")
os.chdir(cu)

os.system("cp caffeine_config.txt /etc/caffeine") 


