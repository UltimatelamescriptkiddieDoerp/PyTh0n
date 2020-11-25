import pyautogui, time

var = 1
time.sleep(15)

while var == 1:
    #pyautogui.press("enter")
    pyautogui.click()
    pyautogui.press("f1")
    time.sleep(2)
    pyautogui.press("f4")
    time.sleep(1)
    pyautogui.click()
    pyautogui.doubleClick()
 
    time.sleep(4)
