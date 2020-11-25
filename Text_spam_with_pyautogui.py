import pyautogui, time, pathlib

time.sleep(10)

t = pathlib.Path.home() / 'Documents' / 'dante.txt'

f = open(t)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(2)