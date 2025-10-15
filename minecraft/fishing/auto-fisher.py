#!/bin/python3
import pyautogui
import pytesseract
from PIL import ImageGrab
import time
import subprocess

while True:
    # grab a region of the screen
    screenshot = ImageGrab.grab(bbox=(1430, 630, 1980, 1080))  # adjust coordinates
    text = pytesseract.image_to_string(screenshot)

    print(text)
    if "obber splashes" in text:
        # pyautogui.mouseDown(button="right")
        # pyautogui.mouseUp(button="right")
        subprocess.run("xdotool click 3",shell=True)
        time.sleep(0.5)
        subprocess.run("xdotool click 3",shell=True) 
        time.sleep(3)
    time.sleep(0.5)

