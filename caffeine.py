import os 
import time
import datetime 
import pyautogui
import sys

sys.path.insert(0 , "/etc/caffeine")
import caffeine_config

type_of_movement = caffeine_config.type_of_movement
mouse_coordinates = caffeine_config.mouse_coordinates
custom_key = caffeine_config.custom_key
delay_time = caffeine_config.delay_time


def mouse_mv():
    pass

def keyboard_mv():
    pass



if type_of_movement == (1) :
    mouse_mv(mouse_coordinates , delay_time)
else :
    keyboard_mv(custom_key , delay_time)