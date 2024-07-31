import os 
import time
import datetime 
import pyautogui
from colorama import Fore
import sys


os.system("clear")

def typography ():
    return Fore.LIGHTBLACK_EX + """ ▄▀▀ ▄▀▄ █▀ █▀ ██▀ █ █▄ █ ██▀
 ▀▄▄ █▀█ █▀ █▀ █▄▄ █ █ ▀█ █▄▄
""" + Fore.WHITE

def ctime() :
    cu = datetime.datetime.now()
    time = cu.strftime('%H:%M %p')
    return time

sys.path.insert(0 , "/etc/caffeine")
import caffeine_config as cf_conf


def move_mouse():
    while True:
        mover = pyautogui.moveTo(cf_conf.mouse_coordinates[0] , cf_conf.mouse_coordinates[1])
        time.sleep(cf_conf.delay_time)

def press_key():
    while True:
        press = pyautogui.press(cf_conf.custom_key)
        time.sleep(cf_conf.delay_time)


if cf_conf.type_of_movement == ("MOUSE") :
    print(typography())
    print(f"Type of movement : Move mouse , Start Time : {ctime()}")
    print(f"The Length : {cf_conf.mouse_coordinates[0]} , The Width : {cf_conf.mouse_coordinates[1]}")
    print(Fore.LIGHTBLACK_EX + "========================================================" + Fore.WHITE)
    move_mouse()

else :
    print(typography())
    print(f"Type of movement : Press key , Start Time : {ctime()}")
    print(f"Custom Keyboard Key : {cf_conf.custom_key}")
    print(Fore.LIGHTBLACK_EX + "========================================================" + Fore.WHITE)
    press_key()
    