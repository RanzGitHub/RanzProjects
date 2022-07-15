import pyautogui as p
import time
import random
from hashlib import sha256
def search(query):
    p.hotkey("ctrl", "e")
    time.sleep(.1)
    p.write(query)
    p.press("enter")
    time.sleep(.67)
def imageFind(image,g,double):
    a = 0
    b = 0
    while(a==0 and b==0):
        try:
            a,b = p.locateCenterOnScreen(image,confidence=0.65 ,grayscale=g)
        except TypeError:
            pass
    if double == True:
        p.doubleClick(a,b)
    else:
        p.click(a,b)
    return a,b
passw = p.password("Enter password: ")
while(sha256(passw.encode('utf-8')).hexdigest() != "hash"):
    print("Wrong password")
    passw = p.password("Enter password: ")
p.hotkey("win","d")
imageFind("Edge.JPG",False,True)
time.sleep(3)
p.hotkey("win","up")
search("bing")