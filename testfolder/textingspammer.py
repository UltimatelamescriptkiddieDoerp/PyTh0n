import pyautogui, time, pathlib

time.sleep(10)

t = pathlib.Path.home() / 'Documents' / 'mango.txt'

f = open(t)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(2)