import os
import colorama

os.system("pip install pyautogui")
os.system("pip install pyinstaller")

os.system("pyinstaller --onefile caffeine.py")
os.chdir("dist")
os.system("cp caffeine /bin")


os.chdir("/etc")
os.mkdir("caffeine")
os.chdir("caffeine")

os.system("cp caffeine_config.py /etc/caffeine")


