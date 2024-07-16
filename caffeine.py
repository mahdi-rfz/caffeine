import os 
import time
import datetime 
import pyautogui
import sys


os.system("clear")

def typography ():
    return """ ▄▀▀ ▄▀▄ █▀ █▀ ██▀ █ █▄ █ ██▀
 ▀▄▄ █▀█ █▀ █▀ █▄▄ █ █ ▀█ █▄▄
"""

def ctime() :
    cu = datetime.datetime.now()
    time = cu.strftime('%H:%M %p')
    return time


sys.path.insert(0 , "/etc/caffeine")
import caffeine_config

type_of_movement = caffeine_config.type_of_movement
mouse_coordinates = caffeine_config.mouse_coordinates
custom_key = caffeine_config.custom_key
delay_time = caffeine_config.delay_time



def mouse_mv(mouse_crd , dl_time):
    pyautogui.moveTo(mouse_crd[0] , mouse_crd[1])
    time.sleep(dl_time)
    
    mouse_mv(mouse_coordinates , delay_time)



def keyboard_mv(ckey , dl_time):
    pyautogui.typewrite(ckey)
    time.sleep(dl_time)
    
    keyboard_mv(custom_key , delay_time)



if type_of_movement == (1) :
    print(typography())
    print(f"Time : {ctime()} , Type of movement : move mouse")
    print(f"Moveto : {mouse_coordinates}")
    print(f"Press ctrl + c for stop and exit")
    print("_______________________________")
    mouse_mv(mouse_coordinates , delay_time)
    
else :
    print(typography())
    print(f"Time : {ctime()} , Type of movement : press key")
    print(f"Press key : {custom_key}")
    print(f"Press ctrl + c for stop and exit")
    print("_______________________________")
    keyboard_mv(custom_key , delay_time)
    