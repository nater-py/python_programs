import pynput
from pynput.mouse import Button, Controller
import pyautogui as pyg
import keyboard 
import time



pyg.FAILSAFE=False

# Placing Block Function
# 'x' Parameter takes Int; Specify how many blocks to place 

def blockPlace(x):
    for i in range(0, x):
        i = 0

        time.sleep(0.5)
        pyg.rightClick(x=0,y=0) # Sends mouse input to right-click to place block
        keyboard.press('s') # Pressing 'd' key to move to right
        time.sleep(0.2) # Delay for in-game user to move
        keyboard.release('s')  # Releasing 'd' key to stop movement 

        i+=1 # Increments 'i' by 1

blockPlace(7) # Places 'x' blocks

def moveLeft():
    keyboard.press('a') # Pressing 'd' key to move to right
    time.sleep(0.5) # Delay for in-game user to move
    keyboard.release('a')  # Releasing 'd' key to stop movement 

moveLeft()

mouse = Controller()
print('The current pointer position is {0}'.format(mouse.position))
mouse.position = (180, 0)

# Turn character to the right using 'turn 90 degrees'  
# Move character to the left
# Call blockPlace function 
   
