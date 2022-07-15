import locale
import subprocess
import os
import time
import warnings
import webbrowser
import pyttsx3
import wikipedia
import requests
from tkinter import *
RWindow = Tk()
RSpeaker = pyttsx3.init()
voices = RSpeaker.getProperty("voices")
def write(Text):
    print(Text)
def launchAnApp(app):
    subprocess.run(app)
def shutdownMyComputer():
    os.system("shutdown /s /t 0")
def restartMyComputer():
    os.system("shutdown /r /t 0")
def launchAWebsite(website):
    webbrowser.open(website)
def speak(Text):
    RSpeaker.say(Text)
    RSpeaker.runAndWait()
def SetMaleVoice():
    RSpeaker.setProperty("voice", voices[0].id)
def SetFemaleVoice():
    RSpeaker.setProperty("voice", voices[1].id)
def Search(WikipediaSearch):
    write(wikipedia.summary(WikipediaSearch))
def wait(secs):
    time.sleep(secs)
def makePlainWindow():
    RWindow.mainloop()
def readtxtFile(txtfile):
    f = open(f"C:\\Users\\risha\\PycharmProjects\\RanzProjects\\{txtfile}")
    count = 0
    for i in f.readlines():
        count = count + 1
        write("Line : " + str(count) + " - " + i)
def countTillNumber(number):
    for NUMBER in range(number):
        write(NUMBER)
