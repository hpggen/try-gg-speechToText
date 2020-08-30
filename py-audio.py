# https://pypi.org/project/SpeechRecognition/1.2.3/

# pip install SpeechRecognition

import pyaudio


# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr


r = sr.Recognizer()

r.energy_threshold = 4000


with sr.Microphone() as source:                # use the default microphone as the audio source
    # listen for the first phrase and extract it into audio data
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition
    # print("You said " + r.recognize(audio))
    # Err:
    #     AttributeError: 'Recognizer' object has no attribute 'recognize'
    # https://stackoverflow.com/questions/34733871/attributeerror-recognizer-object-has-no-attribute-recognize
    # print("Speech was:" + r.recognize_google(audio))
    # print("Speech was:" + r.recognize_google(audio, language="en-us", show_all=False))
    print("Speech was:" + r.recognize_google(audio, language="th-TH", show_all=False))

except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
