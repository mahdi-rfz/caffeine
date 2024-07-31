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

file = open("/etc/caffeine/caffeine_config.txt" , "r")
file = eval(file.read())


def move_mouse():
    while True:
        mover = pyautogui.moveTo(file["mouse_coordinates_x"] , file["mouse_coordinates_y"])
        time.sleep(file["delay_time"])

def press_key():
    while True:
        press = pyautogui.press(file["custom_key"])
        time.sleep(file["delay_time"])


if file["type_of_movement"] == ("MOUSE") :
    print(typography())
    print(f"Type of movement : Move mouse , Start Time : {ctime()}")
    print(f"The Length : {(file)['mouse_coordinates_x']} , The Width : {(file)['mouse_coordinates_y']} , Delay Time : {(file)['delay_time']}")
    print(Fore.LIGHTBLACK_EX + "========================================================" + Fore.WHITE)
    move_mouse()

else :
    print(typography())
    print(f"Type of movement : Press key , Start Time : {ctime()}")
    print(f"Custom Keyboard Key : {file['custom_key']} , Delay Time : {(file)['delay_time']}")
    print(Fore.LIGHTBLACK_EX + "========================================================" + Fore.WHITE)
    press_key()