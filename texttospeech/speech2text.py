import pyttsx3
import speech_recognition as sr

def getSpeech():
    recogniser = sr.Recognizer()
    with sr.Microphone() as source:
        print("Welcome Sir, talk to me")
        audio = recogniser.listen(source)
        print('done!')

    try:
        text = recogniser.recognize_google(audio)
        print("You said ", text)

    except Exception as e:
        print(e)

getSpeech()