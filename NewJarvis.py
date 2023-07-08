import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import requests
import webbrowser
import subprocess
import os
import wikipedia
import time
import pyautogui
import soco
import googletrans
import sys, socket, select
#import pywhatkit
import azure.cognitiveservices.speech as speechsdk
from argparse import ArgumentParser
from tkinter import *
from tkinter import messagebox
from textblob import TextBlob
translator = googletrans.Translator()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

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
            talk("Powering off.")
            exit()
    except Exception:
        query = 'None'
    print(query)
    return query

#Definitions
def printandtalk(Text):
    print(Text)
    talk(Text)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return sentiment, polarity, subjectivity

while True:
    answer = take_user_input()
    sentiment, polarity, subjectivity = analyze_sentiment(answer)
    print(sentiment, "sentence")
    if answer == "hello Jarvis" or answer == "hi Jarvis" or answer == "hello" or answer == "hi":
        talk("Hello Sir.")
    if answer == "Jarvis" or answer == "hey Jarvis":
        talk("Yes sir?")
    if answer == "what time is it":
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {strTime} sir.")
    if answer == "what is the date":
        strDate = datetime.datetime.now().strftime("%m %d %y")
        talk(f"The current date is {strDate} sir.")
    if answer == "shut down my computer":
        talk("Shutting Down Computer sir.")
        os.system("shutdown /s /t 0")
    if answer == "restart my computer":
        talk("Restarting Computer sir.")
        os.system("shutdown /r /t 0")
    if answer == "turn off Jarvis":
        talk("Powering off.")
        exit()
    if answer == "search on Wikipedia":
        talk("What do you want me to search?")
        wikisearch = take_user_input()
        printandtalk(wikipedia.summary(wikisearch))
    if answer == "play a song" or answer == "Play the song":
        talk("What is the name of the song?")
        song = take_user_input()
        pywhatkit.playonyt(song)
        pg.click(x=100, y=100)
    elif answer == "None":
        pass
    if answer == "launch Jarvis messenger":
        talk("Launching JarvisMessenger")
        webbrowser.open("https://botmake.io/JarvisAI")
    if answer == "launch fortnite" or answer == "open Fortnite":
        talk("Launching Fortnite")
        webbrowser.open("https://www.xbox.com/en-US/play/games/fortnite/BT5P2X999VH2")
    if answer == "launch Tubi" or answer == "open Tubi":
        talk("Launching Tubi")
        webbrowser.open("tubitv.com")
    if answer == "search a movie on Tubi":
        talk("What do you want me to search?")
        movie = take_user_input()
        webbrowser.open(f"https://www.tubitv.com/search/{movie}")
    if answer == "launch Netflix" or answer == "open Netflix":
        talk("Launching Netflix")
        webbrowser.open("https://www.netflix.com")
    if answer == "search a movie on Netflix":
        talk("What do you want me to search?")
        movie = take_user_input()
        webbrowser.open(f"https://www.netflix.com/search/{movie}")
    if answer == "launch YouTube" or answer == "open YouTube":
        talk("Launching YouTube")
        webbrowser.open("https://www.youtube.com")
    if answer == "search a video on YouTube":
        talk("What do you want me to search?")
        video = take_user_input()
        webbrowser.open(f"https://www.youtube.com/results?search_query={video}")
    if answer == "play a video on YouTube" or answer == "can I watch a video" or answer == "play something on Youtube":
        talk("What is the name of the video?")
        video = take_user_input()
        pywhatkit.playonyt(video)
        pyautogui.click(x=5000, y=500)
    if answer == "search something on the web":
        talk("What do you want to search?")
        web = take_user_input()
        webbrowser.open(web)
    if answer == "good morning" or answer == "good morning Jarvis":
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"Good Morning Sir, its {strTime} right now.")
    if answer == "wake up Jarvis":
        talk("Online and ready sir.")
    if answer == "sleep Jarvis":
        talk("Ok, I am going to sleep sir.")
    if answer == "thank you" or answer == "thanks" or answer == "thank you Jarvis":
        talk("Your welcome sir!")
    if answer == "how are you" or answer == "how have you been" or answer == "how are you Jarvis":
        talk("Im good, what about you sir?")
        feeling = take_user_input()
        talk("Ok sir.")
    if answer == "launch an app" or answer == "open an app":
        talk("What kind of app?")
        app = take_user_input()
        os.system(f"{app}.exe")
    if answer == "close an app" or answer == "terminate an app" or answer == "destroy an app":
        talk("What kind of app?")
        app = take_user_input()
        os.system(f"taskkill/im {app}.exe")
    if answer == "what is the weather" or answer == "what is the weather outside":
        fah = 'https://api.openweathermap.org/data/2.5/weather?zip=85297,us&appid=252fbbc557951b9b03a9dafe21fc409d&units=imperial'
        cel = 'https://api.openweathermap.org/data/2.5/weather?zip=85297,us&appid=252fbbc557951b9b03a9dafe21fc409d&units=metric'
        api_key = '252fbbc557951b9b03a9dafe21fc409d'
        response = requests.request('GET', fah, headers={})
        response2 = requests.request('GET', cel, headers={})
        data = response.json()
        data2 = response2.json()
        fahrenheit = int(data['main']['temp'])
        celsius = int(data2['main']['temp'])
        talk("The current weather is" + str(fahrenheit) + "degrees fahrenheit" + "and" + str(celsius) + "degrees celsius")
    if answer == "where am I" or answer == "what is my location":
        ip_add = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_q = requests.get(url)
        geo_d = geo_q.json()
        state = geo_d['city']
        country = geo_d['country']
        talk(f"Sir, you are now in {state,country}.")
    if answer == "search a Pokemon" or answer == "search up Pokemon":
        talk("Which Pokémon?")
        pokemon = take_user_input()
        webbrowser.open(f"https://www.pokemon.com/us/pokedex/{pokemon}")
        printandtalk(wikipedia.summary(pokemon))
    if answer == "I'm bored" or answer == "what can I do":
        boredurl = 'https://boredapi.com/api/activity'
        response = requests.request('GET', boredurl, headers={})
        dothiswhenyourbored = response.json()
        thingtodowhenyourbored = dothiswhenyourbored['activity']
        printandtalk("You can " + str(thingtodowhenyourbored))
    if answer == "turn on the light Jarvis" or answer == "turn on the lights Jarvis" or answer == "turn on the lights" or answer == "turn on the light" or answer == "lights":
        os.system("cmd /c wizlight on --ip 192.168.0.84 --k 3000 --brightness 255")
    if answer == "turn off the light Jarvis" or answer == "turn off the lights Jarvis" or answer == "turn off the lights" or answer == "turn off the light":
        os.system("cmd /c wizlight off --ip 192.168.0.84")
    if answer == "make the light blink Jarvis" or answer == " make the lights blink Jarvis" or answer == "make the lights blink" or answer == "make the light blink":
        talk("How many times?")
        blink = take_user_input()
        for b in range(int(blink)):
            time.sleep(0.5)
            os.system("cmd /c wizlight on --ip 192.168.0.84 --k 3000 --brightness 255")
            time.sleep(0.5)
            os.system("cmd /c wizlight off --ip 192.168.0.84")
            time.sleep(0.5)
    if answer == "dim the lights Jarvis" or answer == "dim the light Jarvis" or answer == "dim the lights" or answer == "dim the light":
        talk("What brightness level")
        brightness = take_user_input()
        os.system(f"cmd /c wizlight on --ip 192.168.0.84 --k 3000 --brightness {brightness}")
    elif answer == "full brightness Jarvis" or answer == "full brightness":
        os.system(f"cmd /c wizlight on --ip 192.168.0.84 --k 3000 --brightness 255")
    if answer == "turn on my Xbox" or answer == "turn on Xbox" or answer == "turn on Xbox Jarvis" or answer == "turn on my Xbox Jarvis" or answer == "turn on the Xbox" or answer == "turn on the Xbox Jarvis":
        XBOX_PORT = 5050
        XBOX_PING = "dd00000a000000000000000400000002"

        py3 = sys.version_info[0] > 2


        def main():
            parser = ArgumentParser(description="Send power on packets to a Xbox One.")
            parser.add_argument('-a', '--address', dest='ip_addr', help="IP Address of Xbox One", default='')
            parser.add_argument('-i', '--id', dest='live_id', help="Live ID of Xbox One", default='')
            parser.add_argument('-f', dest='forever', help="Send packets until Xbox is on", action='store_true')
            parser.add_argument('-p', '--pingonly', dest='pingonly', help="Send ping to Xbox One without turning on",
                                action='store_true')
            args = parser.parse_args()

            if not args.ip_addr:
                args.ip_addr = '192.168.0.39'

            if not args.live_id:
                args.live_id = 'F4001CFD5E8A8DD7'

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setblocking(0)
            s.bind(("", 0))
            s.connect((args.ip_addr, XBOX_PORT))

            if isinstance(args.live_id, str):
                live_id = args.live_id.encode()
            else:
                live_id = args.live_id

            if not args.pingonly:
                power_payload = b'\x00' + chr(len(live_id)).encode() + live_id.upper() + b'\x00'
                power_header = b'\xdd\x02\x00' + chr(len(power_payload)).encode() + b'\x00\x00'
                power_packet = power_header + power_payload
                print("Sending power on packets to {0}...".format(args.ip_addr))
                send_power(s, power_packet)

                print("Xbox should turn on now, pinging to make sure...")
            ping_result = send_ping(s)

            if ping_result:
                print("Ping successful!")
            else:
                print("Failed to ping Xbox :(")
                result = ""
                if not args.forever and not args.pingonly:
                    while result not in ("y", "n"):
                        result = user_input("Do you wish to keep trying? (y/n): ").lower()
                if args.forever or result == "y":
                    if not args.pingonly:
                        print("Sending power packets and pinging until Xbox is on...")
                    else:
                        print("Sending pinging until Xbox is on...")
                    while not ping_result:
                        if not args.pingonly:
                            send_power(s, power_packet)
                        ping_result = send_ping(s)
                        print("Failed to ping Xbox :(")
                    print("Ping successful!")

            s.close()


        def send_power(s, data, times=5):
            for i in range(0, times):
                s.send(data)
                time.sleep(1)


        def send_ping(s):
            s.send(bytearray.fromhex(XBOX_PING))
            return select.select([s], [], [], 5)[0]


        def user_input(text):
            response = ""

            while response == "":
                if py3:
                    response = input(text)
                else:
                    response = raw_input(text)

            return response


        if __name__ == "__main__":
            main()
    if answer == f"prime or composite":
        talk("Please type in your number")
        number = (int(input("Enter a natural number")))
        if number < 1:
            talk("Number needs to be greater than 1")
        elif number == 1:
            talk(f"{number} is neither prime nor composite")
        else:
            for divisor in range(2, (number // 2) + 1):
                if (number % divisor) == 0:
                    talk(f"{number} is a Composite Number")
                    break
            else:
                talk(f"{number} is a Prime Number")
    if answer == "translate something" or answer == "translate something Jarvis":
        talk("What language do you want me to translate to?")
        languagetotranslate = take_user_input()
        def recognize_from_microphone():
            # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
            speech_translation_config = speechsdk.translation.SpeechTranslationConfig(
                subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
            speech_translation_config.speech_recognition_language = "en-US"

            target_language = languagetotranslate
            speech_translation_config.add_target_language(target_language)

            audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
            translation_recognizer = speechsdk.translation.TranslationRecognizer(
                translation_config=speech_translation_config, audio_config=audio_config)

            talk("Speak into your microphone.")
            translation_recognition_result = translation_recognizer.recognize_once_async().get()

            if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
                printandtalk("Recognized: {}".format(translation_recognition_result.text))
                printandtalk("""Translated into '{}': {}""".format(
                    target_language,
                    translation_recognition_result.translations[target_language]))
            elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
            elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = translation_recognition_result.cancellation_details
                print("Speech Recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")


        recognize_from_microphone()