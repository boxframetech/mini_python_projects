import pyttsx3

user_say = input("Type a word for the system to speak")

engine = pyttsx3.init()
engine.say(user_say)
engine.runAndWait()

