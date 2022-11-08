import pyttsx3
engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

command = input('Type your voice command\n') 

engine.say(command)
engine.runAndWait()
engine.stop()