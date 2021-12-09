import audioop
from os import set_inheritable
import pyttsx3  #to convert text to speech
import datetime #to get date and time
import speech_recognition as sr #to recognize voice
import wikipedia #to search on wikipedia
import webbrowser #to open websites directly
import os #to use OS functions
from selenium_web import *  #for automation
from selenium_web import infow  
from yt_auto import * #youtube automation
import smtplib #for sending mails


#Dictionary to save names and email-ids
file=open("dict.txt")
dict={}
name =""
email=""
for line in file:
    name,email = line.split('-')
    name=name.lower()
    dict[name]=email


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
# print(voices)
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#Function to send email
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com','password-here')
    server.sendmail('your-email@gmail.com',to,content)
    server.close()

#Function to speak the information
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Function to wish according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi!I am MERLIN , what can i do for you ? ") 


def takeCommand():
    # It takes mic input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e) commented this out to hide errors on the console or terminal.
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia... Please wait ...')
            query=query.replace("wikipedia","")

            try:                    
                assist= infow()
                assist.get_info(query)

            except Exception as e:
                results = wikipedia.summary(query ,sentences =1)  
                speak("According to wikipedia..") 
                speak(results)


        elif 'information' in query:
            speak('Information about which topic...? ')
            query = takeCommand().lower()
            results = wikipedia.summary(query ,sentences = 1)  
            speak("According to wikipedia") 
            try:                    
                print(results)
                speak(results)
            except Exception as e:
                speak(results)


        elif ('send an email' in query or 'send email' in query or 'email' in query or 'mail' in query):
            try:
                speak("Send email to whom...Speak the name of person to find in the database ?")
                name=takeCommand().lower()
                print("Recepient's Email ID --> ",dict[name])
                speak("What should i write in email ? ")
                content=takeCommand()
                to=dict[name]
                sendEmail(to,content)
                speak("Email sent ...!")
            except Exception as e:
                speak("I couldn't find the person in the database , would you like to enter their email address down below... ? ")
                ans=takeCommand().lower()
                if('yes' in ans):
                    speak("Enter the email down below...")
                    to=input("Enter the Email ID : ")
                    speak("What should i write in email ? ")
                    content=takeCommand()
                    sendEmail(to,content)
                    speak("Email sent successfully .")
                else:
                    print(e)
                    speak("Sorry , couldn't send the email , what else can i do for you  ? ")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam , The time is {strTime}")

        elif 'play' and 'video' in query:
            speak("Which video should i play specifically....?")
            query = takeCommand().lower()
            speak("Searching for the video on youtube ... please wait...")
            try:
                assist=video()
                assist.play(query)

            except Exception as e:
                speak("sorry i couldn't find the video you were looking for... please try once again...")

        elif 'how' and 'are' and 'you' in query:
            speak("I am programmably fine mam ! , what can i do for you ??")

        elif 'quit' in query:
            speak('BYE BYE ...')
            break
        elif 'stop' in query:
            speak('Sayonara...')
            break

        elif 'exit' in query:
            speak('Signing off... have a great day ahead..')
            break

        else:
            speak("I couldn't understand ... Please say it again...")

        
