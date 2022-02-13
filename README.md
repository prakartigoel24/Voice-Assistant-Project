# MERLIN - Voice Assistant


Created a voice assistant for everyday tasks which can be done by using voice commands only .
This has a specific set of tasks which the voice assistant can perform , with option of upgradation in future to add more tasks.


 ## * TASKS * ##

---> Opening various websites 

---> Getting some information from web 

---> Playing videos on Youtube 

---> Sending mails 
<hr>

### This project is developed in PYTHON using various fuctions and Modules available. ###

- Developed using Speech Recognition 

-  selenium\_web and Speech to Text libraries in Python.

- Used pyttsx3 to convert text to speech and speech-recognition for speech manipulation and recognition tasks.

- Used selenium web driver to automate tasks like searching for information on wikipedia and playing videos on Youtube.

- Used Smtplib module of python to create an Email sending function which used SMTP (simple mail transfer protocol) to send and route emails between mail servers.


# Steps To Run This Project On Your Device : #

1.Install python-3.8 (64 bit) or above from 'https://www.python.org/downloads/' and add the PATH to your USER and System Variables under Environment variables. 

2.Install VS Code or PyCharm or any other IDE your'e comfortable with.

3.Clone this repository on your device.

4.Install the following packages using the 'pip install (package name)' command.

PACKAGES : 

            -> import audioop                                       #for audio related tasks
            -> from os import set_inheritable                       #to use Set inheritable function of OS
            -> import pyttsx3                                       #to convert text to speech
            -> import datetime                                      #to get date and time
            -> import speech_recognition as sr                      #to recognize voice
            -> import wikipedia                                     #to search on wikipedia
            -> import webbrowser                                    #to open websites directly
            -> import os                                            #to use OS functions
            -> from selenium_web import *                           #for automation 
            -> from yt_auto import *                                #youtube automation
            -> import smtplib                                       #for sending mails

            
4.NOW YOURE ALL SET. Woohoo !!!

**IMPORTANT**
-Write the names and Email IDs of people separated via a "-" in the dict.txt file to use their names to send Email to their respective Email IDs.
