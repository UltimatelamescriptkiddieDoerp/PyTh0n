import pyautogui, time
from random import randint

var = 1

print("Automatischer Hauskauf startet in 30sec")
time.sleep(30)
print("Automatischer Hauskauf beginnt")

while var == 1:
    pyautogui.press("num0")
    time.sleep(1)
    pyautogui.press("num0")
    time.sleep(1)
    pyautogui.press("num0")
    time.sleep(1)
    pyautogui.press("num4")
    time.sleep(1)
    pyautogui.press("num0")
    time.sleep(3)