import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<=17:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Hello sir I am Jarvas How can i help u")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listinng.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizating...")
        qury = r.recognize_google(audio, language='en-in')
        print(f'user said : {qury}')

    except Exception as e:
        print("Say that again")
        return "None"

    return qury

if __name__ == '__main__':

    # wishme()
    takecommand()