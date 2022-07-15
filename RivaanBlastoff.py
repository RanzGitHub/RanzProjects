import pyttsx3
import time
laucherman = pyttsx3.init()
voices = laucherman.getProperty('voices')
laucherman.setProperty("rate", 140)
laucherman.setProperty('voice', voices[0].id)
laucherman.say("3")
time.sleep(1)
laucherman.say("2")
time.sleep(1)
laucherman.say("1")
time.sleep(1)
laucherman.say("Blastoff")
laucherman.runAndWait()