# Steps 

# Define width, length (6x6)
# Place block, move backward (Loop 6 times)

import pyautogui
import pynput
import keyboard 
import time
import pyautogui as pyg

pyautogui.FAILSAFE=False

while keyboard.is_pressed('q') == False:
    time.sleep(5)
    pyg.rightClick(x=0,y=0)

    if keyboard.is_pressed('q') == True: 
        break
    else:
        continue


