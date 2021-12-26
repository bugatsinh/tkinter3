# WHEN I AM FREE DO WILL THIS



import pyttsx3
import speech_recognition as sr
# pip install speechRecognition

import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good Morning!")

    elif hour >= 12 and hour < 18:
        speak("good Afternoon!")
    else:
        speak("good Evening")
    speak("I am jarvis sir. plese tell me how may I help you")


def takeCommand():
    #  it takes microphone input fron the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        Quary = r.recognize_google(audio, language='en-in')
        print(f"user said {Quary}\n")

    except Exception as e:
        # print(e)
        print("say that again plese...")
        return "None"
    return Quary


if __name__ == "__main__":
    wishMe()
    takeCommand()

