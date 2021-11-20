import pyautogui
import pynput
import keyboard 
import time
import pyautogui as pyg

pyautogui.FAILSAFE=False

# Placing Block Function
# 'x' Parameter takes Int; Specify how many blocks to place 

def blockPlace(x):
    for i in range(0, x):
        i = 0

        time.sleep(2)
        pyg.rightClick(x=0,y=0)
        
        i+=1

        if keyboard.is_pressed('q') == True: 
            break
        else:
            continue

blockPlace(7)