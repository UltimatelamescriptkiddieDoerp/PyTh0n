import pyautogui, time
from random import randint


var = 1
Zufallszahl = randint(65, 180)
ran = randint(1, 12)
randomtime = randint(2, 6)


time.sleep(10)

while var == 1:
    pyautogui.write(":-battle")
    pyautogui.press("enter")
    time.sleep(randomtime)
    if ran == 1:
        pyautogui.write(":-i")
        pyautogui.press("enter")
        time.sleep(randomtime)
    if ran == 2:
        pyautogui.write(":-s")
        pyautogui.press("enter")
        time.sleep(randomtime)
    if ran == 3:
        pyautogui.write("ich geh ab wie kackige Kacke")
        pyautogui.press("enter")
        time.sleep(randomtime)
    if ran == 4:
        pyautogui.write("uiuiui")
        pyautogui.press("enter")
        time.sleep(randomtime)
    time.sleep(Zufallszahl)