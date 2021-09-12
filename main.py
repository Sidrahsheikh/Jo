
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wiki
import pyjokes
import os
import sys as sy
import wolframalpha
import time as t
import requests
import webbrowser
import tkinter as tk
from tkinter import *

HEIGHT = 500
WIDTH = 500

def take_command():
    try:
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            listener.non_speaking_duration = 1
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source,duration= 1)
            voices = listener.listen(source)
            command = listener.recognize_google(voices , language= 'en-in')
            command = command.lower()

            print(command)
    except :
        pass
        talk('Please say it again')
        return 'None'
    return command

def talk(text):
    engine = pyttsx3.init( )
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def hello() :
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and  hour < 12:
        talk('Good Morning')
    elif(hour >= 12 and hour < 18):
        talk('Good Afternoon')
    else:
        talk('Good Evening')

    talk('I am Jo')
    talk('how can I help you ?')

def run_jo():

    command = take_command()
    if 'play' in command:
        song=command.replace('play', '')
        talk('Playing'+song)
        print('Playing'+song)
        pywhatkit.playonyt(song)

    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)

    elif 'search for' in command:
        person = command.replace('search for', '')
        talk('Searching Wikipedia...')
        info = wiki.summary(person,3)
        print(info)
        talk('According to Wikipedia')
        talk(info)

    elif 'laugh' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'open youtube' in command:
        talk('Opening youtube')
        print('Opening youtube')
        webbrowser.open('https://www.youtube.com/')

    elif 'open google' in command:
        talk('Opening google')
        print('Opening google')
        webbrowser.open('https://www.google.com/')


    elif 'open stack overflow' in command:
        talk('Opening stackoverflow')
        print('Opening stackoverflow')
        webbrowser.open('https://stackoverflow.com/')

    elif 'open code blocks' in command:
        talk('Opening code blocks')
        print('Opening code blocks')
        codepath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
        os.startfile(codepath)

    elif 'open pycharm' in command:
        talk('Opening pycharm')
        print('Opening pycharm')
        codepath = "C:\\Users\\Sidra sheikh\\PyCharm Edu 2020.3.1\\bin\\pycharm64.exe"
        os.startfile(codepath)

    elif 'are you there' in command:
        talk('Always at your service Maam')
    elif 'how are you' in command:
        talk('I am fine ,thank you Maam ')
        talk('How are you maam')
    elif 'who created you' in command:
        talk('I have been created by Sidra')
    elif 'who are you' in command:
        talk('I am your desktop assistant. My name is JO.')

    elif 'shutdown the PC' in command:
        choice = input("Please confirm to shutdown the pc (y or n)")
        if choice == 'no':
            exit()
        else:
            os.system("shutdown /s /t 1")

    elif 'bus bahut hua band karo' in command:
        sy.exit(talk("Ok Sid, Take Care."))
        
    elif 'wait' in command:
        talk(" for how much time you want to stop jo from listening")
        a = int(take_command())
        t.sleep(a)
        print(a)
        talk('Okay ,lets resume')

    elif "write a note" in command:
            talk("What should i write, sir")
            note = take_command()
            file = open('jarvis.txt', 'w')
            talk("Sir, Should i include date and time")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

    elif "show note" in command:
            talk("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            talk(file.read(6))

    elif 'where is' in command :
            command = command.replace("where is", "")
            location = command
            talk("User asked to Locate")
            talk(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

    elif "weather" in command:

            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            talk(" City name ")
            print("City name : ")
            city_name = take_command()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))

            else:
                talk(" City Not Found ")
    elif "calculate" in command:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = command.lower().split().index('calculate')
            query = command.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            talk("The answer is " + answer)

    elif "what is" in command or "who is" in command:
            client = wolframalpha.Client("API_ID")
            res = client.query(command)

            try:
                print (next(res.results).text)
                talk (next(res.results).text)
            except StopIteration:
                print ("No results")
    else :
        talk('Please say it again.')

if __name__ == '__main__':

    root = tk.Tk()
    root.title("My desktop Assistant : JO  ")
    bg = PhotoImage(file = "JO.png")

    canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
    canvas.pack(fill ='both',expand = True)
    canvas.create_image(0,0,image =bg,anchor ='nw')
    B=tk.Button(root,text ='Click Me',bg ='gray3',fg ='white')
    B.pack()
    B.bind("<Button>",lambda e : run_jo())
    hello()
    root.mainloop()
