# https://pypi.org/project/SpeechRecognition/1.2.3/

import pyaudio

import time
import speech_recognition as sr


# this is called from the background thread
def callback(recognizer, audio):
    try:
        # received audio data, now need to recognize it
        # print("You said " + recognizer.recognize(audio))
        print("Speech was:" + r.recognize_google(audio, language="th-TH", show_all=False))
    except LookupError:
        print("Oops! Didn't catch that")


r = sr.Recognizer()

r.energy_threshold = 4000

r.listen_in_background(sr.Microphone(), callback)

while True:
    time.sleep(0.1)
