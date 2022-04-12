import warnings
import pyttsx3
import speech_recognition as sr
import time
t = time.localtime()
import datetime

warnings.filterwarnings("ignore")

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
talk("Hello I'm CopyBot, I can copy any of your words")

while True:
    q = input("")
    talk(q)