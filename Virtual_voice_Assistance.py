import pyttsx3
#this module is use for speak

import datetime
#this module is use to give current date and time

import speech_recognition as sr

""" we need to this module because in our project we need to microphone show
with the help of this module the we get microphone.The  microphone take command
and return it in string form """

import wikipedia
#in program i want to search play music etc. so we need to  wikipedia module.

import webbrowser
#this module is use for search youtube ,google.

import os
#this module is use for allow the all directorey like music in your operating system.






engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') #this command is use to take current voices
#print(voices[1])
engine.setProperty('voice',voices[1].id) #here we set voices type 

def speak(audio):
   engine.say(audio) #here we give command to speak 
   engine.runAndWait() #without this command  speak will not able to use
   
def wishme():
   #this function is use to wish  live time according to you laptop
   _time=int(datetime.datetime.now().hour)
   if _time>=0 and _time<12:
      speak("good morning!")
   elif _time>=12 and _time<18:
      speak("good afternoon!")
   else:
      speak("good night!")
   speak("hello sir i am jarvis how can i hep you!")
   
   
def takeCommand():
    #It takes microphone input from the user and returns string output
   r = sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=8,phrase_time_limit=8)

 
   try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

   except Exception as e:
        print(e)    
        print("Say that again please...")   
        return "None" 
   return query.lower()

#def Task_Gui():
if __name__=="__main__":


        
    wishme()
    while True:
    #if 1:
   
       query = takeCommand().lower()
       #logic for executing task based on program
       
       if 'wikipedia' in query:
          speak("searching wikipedia.....")
          query=query.replace("wikipedia","")#here we replace wikipedia by blank
          results=wikipedia.summary(query,sentences=10)
          speak("According to wikipedia....")
          print(results)
          speak(results)
          
       if 'hello' in query:
          speak("hello... this is Krishnamohan's python based first project what can i hepl.. you sir..")
       
       elif "open youtube" in query:
          speak("opening youtube..")
          webbrowser.open("youtube.com")
          
       elif "open google" in query:
          speak("opening google..")
          webbrowser.open("google.com")
          
       elif "open stackoverflow" in query:
          speak("opening stackoverflow...")
          webbrowser.open("stackoverflow.com")
          
       elif 'play music' in query:
            n=0
            music_dir = 'filr_directory path'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[n]))
            for i in songs:
               if 'next song' in query:
                  music_dir = 'file_directory path'
                  songs = os.listdir(music_dir)
                  print(songs)    
                  os.startfile(os.path.join(music_dir, songs[n+1]))
               break
               
       elif 'time' in query:
          strtime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir..the time is {strtime}")
          print(speak)
          
          
       elif 'open gfg' in query:
          webbrowser.open('https://www.geeksforgeeks.org/')
      
       elif 'exite' in query:
            break
          
       '''elif 'open code' in query:
          codepath=""
          os.startfile(codepath)'''
       #elif 'break' in query:

