import speech_recognition as sr
import pyttsx3




class Speech():
    def __init__(self):
        self.ears = sr.Recognizer()
        self.voice = pyttsx3.init()
        


    def listen(self):

        print("Listening...")
        with sr.Microphone() as source:
            self.ears.adjust_for_ambient_noise(source)
            audio_text = self.ears.listen(source)
            try:
                text = self.ears.recognize_google(audio_text)
                return text
            except:
                return "FAILED"

    def say(self, text):
        self.voice.say(text)
        self.voice.runAndWait()


    def listen_and_respond(self):
        while True:
            self.say(self.listen())


        
