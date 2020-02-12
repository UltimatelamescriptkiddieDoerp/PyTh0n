import zipfile
import itertools
import string
import threading
from threading import Thread
import traceback


def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Succsess: Password is ' + pwd)
    except Exception:
        pass

zipFile = zipfile.ZipFile(" #Hier den Dateipfad inkl. Datei + Dateiendung einfuegen")
myLetters = string.ascii_letters + string.digits + string.punctuation
for i in range(3,30):
    for j in map(''.join, itertools.product(myLetters, repeat=i)):
        t = Thread(target=crack, args=(zipFile, j))
        t.start()