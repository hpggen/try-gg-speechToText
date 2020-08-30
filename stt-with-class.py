# https://stackoverflow.com/questions/51306399/python-speech-recognition-listen-in-background-on-button-press


import time
import speech_recognition as sr


# class VoiceRecognitionWidget(ScriptedLoadableModuleWidget):
class VoiceRecognitionWidget():
    def callback(self, recognizer, audio):
        try:
            # print(recognizer.recognize_google(audio))
            print(recognizer.recognize_google(audio, language="th-TH", show_all=False))
        # handles any api/voice errors  errors
        except sr.RequestError:
            print("There was an issue in handling the request, please try again")
        except sr.UnknownValueError:
            print("Unable to Recognize speech")

    def onApplyButton(self):
        #self.displayLabel.setText("Listening for speech....")

        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 50

        try:
            self.microphone = sr.Microphone()

        except(IOError):
            print("ERROR: No default microphone. Check if microphone is plugged in or if you have a default microphone set in your sound settings.")
            # self.errors.setText(
            #     "ERROR: No default microphone. Check if your microphone is plugged in or if you have a default microphone set in your sound settings.")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            # audio = self.recognizer.listen(source)

        self.stop_listening = self.recognizer.listen_in_background(
            self.microphone, self.callback)

    def stop(self):
        # print(self.stop_listening)
        print(type(self.stop_listening))


xx = VoiceRecognitionWidget()
xx.onApplyButton()
time.sleep(20)
xx.stop()
