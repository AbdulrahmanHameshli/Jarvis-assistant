import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import time as tm
import wikipedia as wk
import smtplib
from email.message import EmailMessage
import webbrowser

engine=pyttsx3.init()
brows=webbrowser



def time():
    speak("Sir, the time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    day= int(datetime.datetime.now().day)
    speak(f"the date today is")
    speak(day)
    speak(month)
    speak(year)

def send_email(massege, to):
    msg=EmailMessage()
    msg.set_content(massege)
    msg["subject"]="Abbes IA"
    msg['to'] = to

    us = "Username"
    msg['from']="Abbes IA"
    pw= "Password" 

    server = smtplib.SMTP('smtp.gmail.com', 587)   #smtp:simple mail transfer protocol, 587 is thr port for tls=Transport Layer Security, krypterande meddelande för säkerhet.
    server.starttls()
    server.login(us,pw)
    server.send_message(msg)
    server.quit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_google():
    brows.open("https://www.google.com/")


def wishme():
    speak("Welcome back sir!")
    tm.sleep(0.5)
    speak("How can i help you, sir")



def wiki(qu):
    quer=qu.replace("means","")
    result= wk.summary(quer,sentences=2)
    print(result)
    speak(result)


def takeComand():
    r= sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =  r.listen(source)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio,language="en-in")
        print(query)


    except Exception as e:
        print(e)
        speak("say that again pleas...!")
        return "None"

    return query

if __name__=="__main__":
    wishme()
    while True:
        query = takeComand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        # if "open Abbe life" in query:
        #     abbes_life()
        elif "kill yourself" in query:
            quit()

        elif "means" in query:
            speak("I am searching sir")
            wiki(query)
        elif "open google" in query:
            open_google()
            speak("Done sir")

        elif "send mail" in query:
            temp =True
            while temp:
                speak("Sir, what do you want me to send?")
                massege=takeComand()
                speak(f'Sir, is it what you said?')
                speak(massege)
                yesOrNo=takeComand()
                if "yes" in yesOrNo:
                    temp= False
                    to="To_person"
                    send_email(massege,to)
                    speak("success")
                else:
                    speak("repete sir")
