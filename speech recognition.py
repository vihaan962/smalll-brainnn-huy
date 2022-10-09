# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:17:53 2022

@author: VIHAAN KATHURIA
"""

from tkinter import*
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from datetime import datetime

root = Tk()
root.geometry("800x600")
root.config(bg = "#deb8db")

title = Label(root,text = "Ask anything to the Nobody",bg = "#deb8db",font = ("URW Chancery L",20,"italic"))
title.place(relx = 0.5,rely = 0.1,anchor = CENTER)
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def r_audio():
    speak("How can I help you ???")
   
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ''
        
        try:
            voice_data = speech_recognisor.recognize_google(audio,language = 'en-in')
        except sr.UnknownValueError:
            print('Please repeat I did not get that')
            speak("Pleae repeat I did not get you")
    respond(voice_data)
    

def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Nobody")
        print("My name is Nobody")
    if "time" in voice_data:
        speak("Current time is :")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print (current_time)
    
    if "search" in voice_data:
        speak("opening google")
        print("opening google")
        webbrowser.get().open("https://www.google.co.in/")
        
    
    if "video" in voice_data:
        speak("opening Youtube")
        print("opening Youtube")
        webbrowser.get().open("https://www.youtube.com/")
        
    if "text editor" in voice_data:
        speak("opening the app")
        print("opening the app")
        subprocess.Popen(["notepad.exe"])        
    
btn = Button(root,text = "speak",command = r_audio,bg = "#deb8db",font = ("Century Schoolbook L",15,"bold"))
btn.place(relx = 0.5,rely = 0.5,anchor = CENTER)
root.mainloop()