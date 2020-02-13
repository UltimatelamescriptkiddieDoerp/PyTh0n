import zipfile
import itertools
import string
import threading
from threading import Thread
import traceback

zipFile = zipfile.ZipFile("/home/doerpi/Downloads/crackmeZIP.zip")       #Hier den Dateipfad inkl. Datei + Dateiendung einfuegen


def bruteforce():
    myLetters = string.ascii_letters + string.digits + string.punctuation
    for i in range(3,30):
        for j in map(''.join, itertools.product(myLetters, repeat=i)):
            t = Thread(target=crack, args=(zipFile, j))
            t.start()

def dictionary():
    passwords = open("/home/doerpi/Downloads/mypwlist")   #hier die zu nuztende PWListe eintragen
    for line in passwords.readlines():
        pwd = line.strip('\n')
        t = Thread(target=crack, args=(zipFile, pwd))
        t.start()
        if threading.active_count() > 500:
                t.join()

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Succsess: Password is ' + pwd)
    except Exception:
        pass

dictionary()



