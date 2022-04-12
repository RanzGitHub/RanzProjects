#JARVISAI
import warnings
import numpy as np
import cv2
import pyttsx3
import requests
import wikipedia
import time
import webbrowser
import sys
import speech_recognition as sr
from playsound import playsound
from pyttsx3 import speak
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *
warnings.filterwarnings("ignore")
t = time.localtime()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("rate", 168)
engine.setProperty('voice', voices[0].id)
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')
        if 'exit' in query or 'stop' in query:
            pyttsx3.speak("OK Sir, I will stop")
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    print(query)
    return query
# These are most of the common definitions
def talk(audio):
    engine.say(audio)
    engine.runAndWait()
def JARVIS_telltime():
    print(t.tm_hour,":",t.tm_min)
def JARVIS_tellday():
    print(t.tm_mday, "of", t.tm_mon)
def JARVIS_telldate():
    print(t.tm_mon,"/",t.tm_mday,"/",t.tm_year)
def JARVIS_said():
    print("jarvis said > ")
def q_Jarviswikisummary():
    print(wikipedia.summary(q_Jarvis2wiki))
def rivaanspell():
    talk("R")
    talk("I")
    talk("V")
    talk("A")
    talk("A")
    talk("N")
# This is the main program
print("Say words to talk to J.A.R.V.I.S")
talk("Hello I'm JARVIS, How may I help you?")
while True:
    q_Jarvis = take_user_input()
    if q_Jarvis == "who are you":
        JARVIS_said()
        talk("I am JARVIS, I am your personal assistant.")
    if q_Jarvis == "what day is it":
        JARVIS_said()
        talk("The current day is")
        print(JARVIS_tellday())
    if q_Jarvis == "what is the date":
        JARVIS_said()
        talk("The current date is")
        print(JARVIS_telldate())
    if q_Jarvis == "what time is it":
        JARVIS_said()
        talk("The current time is")
        print(JARVIS_telltime())
    if q_Jarvis == "play memes :)":
        print("J.A.R.V.I.S playing 3 memes")
        playsound('Coffin Dance Meme - Sound Effect.mp3')
        time.sleep(1)
        playsound('recording1 (3).wav')
        time.sleep(1)
        playsound('Rick Astley - Never Gonna Give You Up (1).wav')
    if q_Jarvis == "spell ryan":
        talk("R")
        talk("Y")
        talk("A")
        talk("N")
    if q_Jarvis == "say ryan":
        JARVIS_said()
        talk("ryan")
    if q_Jarvis == "Play Rick Roll":
        JARVIS_said()
        talk("Opening Rick Roll")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if q_Jarvis == "who built you":
        JARVIS_said()
        talk("I was created by Iron Man but now owned by you")
    if q_Jarvis == "tell me a joke":
        JARVIS_said()
        talk("What happened to the frog's car? It got toad")
    if q_Jarvis == "what do you look like":
        talk("This is what I look like")
        webbrowser.open("https://www.google.com/search?q=jarvis+images&rlz=1C1VDKB_enUS989US989&sxsrf=APq-WBuA-dsGJgd00ls4aIvTR0sXeOQd9A:1649111073013&tbm=isch&source=iu&ictx=1&vet=1&fir=zUONjIhvTjmHmM%252C_uxsqs8ixYCZ5M%252C_%253B5ySo_MZPyb1BKM%252C_uxsqs8ixYCZ5M%252C_%253BfLshT2sUwmf1hM%252C5MbAUgRKftZfCM%252C_%253BYQxanP2FVsiR3M%252C_uxsqs8ixYCZ5M%252C_%253BZsIYX-p3oM41JM%252CAyxVWawPylAxKM%252C_%253BV8owMcodd7PbVM%252Cbw_VFy5MUXPEJM%252C_%253B6ojDOhqIhXK3SM%252CpCwo0XPYEVjvfM%252C_%253B41Uly5vel1HLEM%252C_uxsqs8ixYCZ5M%252C_%253Bs-PPlVGioduNDM%252CAyxVWawPylAxKM%252C_%253BpXkFCi20F_SbMM%252C2qFLpSQ9_XBJSM%252C_%253Bfs30tgVwdh_4FM%252C5MbAUgRKftZfCM%252C_%253BQogxTGYKkeKFLM%252C_uxsqs8ixYCZ5M%252C_&usg=AI4_-kQ1cO1mgRjm1APf-3WO9ZsDReZuxg&sa=X&sqi=2&ved=2ahUKEwjKyc69ufv2AhU7w4sBHfbgCysQ9QF6BAgDEAE")
        talk("These are images of what I look like")
    if q_Jarvis == "launch YouTube":
        JARVIS_said()
        talk("Opening Youtube")
        webbrowser.open("https://youtube.com")
    if q_Jarvis == "launch Netflix":
        JARVIS_said()
        talk("Opening Netflix")
        webbrowser.open("https://netflix.com/browse")
    if q_Jarvis == "launch Amazon music":
        JARVIS_said()
        talk("Opening Amazon music")
        webbrowser.open("music.amazon.com")
    if q_Jarvis == "launch scratch":
        JARVIS_said()
        talk("Opening Scratch Programming Language")
        webbrowser.open("scratch.mit.edu")
    if q_Jarvis == "send virtual hug prank":
        JARVIS_said()
        talk("Opening virtual hug prank")
        webbrowser.open("https://www.youtube.com/watch?v=ES2Wmo_fYxQ")
    if q_Jarvis == "voice = female":
        JARVIS_said()
        print("jarvis said > Voice is female")
        engine.setProperty('voice', voices[1].id)
    if q_Jarvis == "voice = male":
        print("jarvis said > Voice is male")
        engine.setProperty('voice', voices[0].id)
    if q_Jarvis == "play songs for kids":
        JARVIS_said()
        talk("Opening songs for kids")
        webbrowser.open("https://open.spotify.com/search/baby%20song")
    if q_Jarvis == "play a song for adults":
        webbrowser.open("https://open.spotify.com/search/inds")
    if q_Jarvis == "hey Jarvis":
        talk("Yes")
    if q_Jarvis == "play iCarly":
        webbrowser.open("https://www.netflix.com/watch/70147856?trackId=256829969")
        JARVIS_said()
        talk("Playin iCarly")
    if q_Jarvis == "play creeped out":
        webbrowser.open("https://www.netflix.com/watch/81153603?trackId=251884370&tctx=0%2C0%2C6e151a50-cebf-43b9-9f80-b1f061a887ba-610013512%2Cb985a310-fe98-412c-b3fc-63b947943de5_243682744X20XX1649179465078%2Cb985a310-fe98-412c-b3fc-63b947943de5_ROOT%2C%2C%2C")
        JARVIS_said()
        talk("Playin Creeped Out")

    if q_Jarvis == "Wikipedia":
        print("jarvis said > in wikipedia")
        q_Jarvis = input("Search Your Thing")
        print("Type your search")
        q_Jarvis2wiki = input(wikipedia.search(q_Jarvis))
        print(q_Jarviswikisummary())

    def exitwiki():
        print("jarvis said > Out of wikipedia")

    if q_Jarvis == "exit wikipedia":
        print(exitwiki())
    if q_Jarvis == "rivaan":
        while True:
            talk("Rivaan Singh")
            print("Rivaan Singh")
    if q_Jarvis == "play alarm sound":
        playsound('Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3')

    if q_Jarvis == "do I have any messages on Gmail":
        JARVIS_said()
        webbrowser.open("gmail.google.com")
        talk("Opening gMail")
        talk("Looks like you have a lot of messages")
    if q_Jarvis == "launch mystery Doug":
        JARVIS_said()
        webbrowser.open("mysterydoug.com")
        talk("Opening MysteryDoug")
    if q_Jarvis == "turn off Jarvis":
        talk("Ok")
        talk("Turning Off")
        exit()
    if q_Jarvis == "good morning Jarvis":
        talk("Good Morning sir")
    if q_Jarvis == "thanks Jarvis":
        talk("Your Welcome sir")
    if q_Jarvis == "Mark Zuckerberg AI":
        webbrowser.open("https://www.youtube.com/watch?v=ZGLPxEv_EWo")
    if q_Jarvis == "Play Are You Afraid of the Dark":
        JARVIS_said()
        webbrowser.open("https://www.netflix.com/watch/81486553?trackId=256829969")
        talk("Playin Are You Afraid of the Dark")
    if q_Jarvis == "launch tinkercad":
        JARVIS_said()
        webbrowser.open("tinkercad.com/dashboard")
        talk("Opening Tinkercad")
    if q_Jarvis == "launch camera":
        JARVIS_said()
        talk("Opening Jarvis Cam")
        cam = cv2.VideoCapture(0)
        while cam.isOpened():
            ret, CAMERA = cam.read()
            if cv2.waitKey(10) == ord('q'):
                break
            cv2.imshow('J.A.R.V.I.S cam', CAMERA)
    if q_Jarvis == "launch Google Maps":
        webbrowser.open("maps.google.com")
        JARVIS_said()
        talk("Opening Google Maps")
    if q_Jarvis == "launch Google Earth":
        webbrowser.open("earth.google.com")
        JARVIS_said()
        talk("Opening Google Earth")
    #In case you didn't know slither.io is a game.
    if q_Jarvis == "launch slither.io":
        webbrowser.open("https://slither.io/")
        JARVIS_said()
        talk("Opening slither.io")
    # In case you didn't know roblox is a server full of games that you can play for free.
    if q_Jarvis == "launch Roblox":
        webbrowser.open("https://web.roblox.com/home?nu=true")
        JARVIS_said()
        talk("Opening Roblox")
    if q_Jarvis == "launch iceworld simulator":
        JARVIS_said()
        talk("Opening IceWorld Simulator")
        def input(key):
            if key == "escape":
                quit()
        app = Ursina()
        print("Welcome to Ice World")
        Sky(texture='sky_ice')
        player = FirstPersonController()
        app.run()
    if q_Jarvis == "launch Sunset simulator":
        JARVIS_said()
        talk("Opening Sunset Simulator")
        app = Ursina()
        def input(key):
            if key == "escape":
                # Escape Key Pressed... Quit
                quit()
        print("Welcome to Sunset Simulator")
        Sky(texture='sky_sunset')
        player = FirstPersonController()
        app.run()
    if q_Jarvis == "launch Google":
        webbrowser.open("https://google.com")
        JARVIS_said()
        talk("Opening Google")
    if q_Jarvis == "launch my browser":
        JARVIS_said()
        talk("Opening RanzBrowser")
        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl('https://google.com'))
                self.setCentralWidget(self.browser)
                self.showMaximized()
                # Icon
                self.setWindowIcon(QtGui.QIcon('Letter-R-Logo-Vector (1).png'))
                # Background
                self.setStyleSheet("background-color: orange;")
                # Buttons
                navbar = QToolBar()
                self.addToolBar(navbar)
                back_btn = QAction('<', self)
                back_btn.triggered.connect(self.browser.back)
                navbar.addAction(back_btn)
                forward_btn = QAction('>', self)
                forward_btn.triggered.connect(self.browser.forward)
                navbar.addAction(forward_btn)
                refresh_btn = QAction('⟳', self)
                refresh_btn.triggered.connect(self.browser.reload)
                navbar.addAction(refresh_btn)
                home_btn = QAction('Home', self)
                home_btn.triggered.connect(self.navigate_home)
                navbar.addAction(home_btn)
            def navigate_home(self):
                self.browser.setUrl(QUrl('https://google.com'))
        app = QApplication(sys.argv)
        # Name of Browser
        QApplication.setApplicationName('                                                                                                                                                                                RanzBrowser')
        window = MainWindow()
        app.exec_()
    if q_Jarvis == "launch Google snake":
        webbrowser.open("https://www.google.com/fbx?fbx=snake_arcade")
        JARVIS_said()
        talk("Opening Google Snake")
    if q_Jarvis == "launch Google dinosaur":
        webbrowser.open("https://trex-runner.com")
        JARVIS_said()
        talk("Opening Google Dinosaur")
    if q_Jarvis == "play boruto theme":
        webbrowser.open("https://www.youtube.com/watch?v=48wCQXl83-s")
        JARVIS_said()
        talk("Opening Boruto's Theme")
    if q_Jarvis == "who is the owner of Jarvis":
        JARVIS_said()
        talk("The owner of me is Rishaan Singh")