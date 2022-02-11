import pyttsx3  
import speech_recognition as sr   
import datetime   
import os 
import xlwt
from xlwt import Workbook

MASTER = 'Vipin kumar sir'
i=0
voice_id=0
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
newVoiceRate = 145  
engine.setProperty('rate',newVoiceRate)  
engine.setProperty('voice', voices[voice_id].id) 

wb = Workbook()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('\nGood morning '+MASTER+'\n')
        speak('Good morning'+MASTER)

    elif hour >= 12 and hour < 18:
        print('good afternoon '+MASTER+'\n')
        speak('good afternoon'+MASTER)

    else:
        print('good evening '+MASTER+'\n')
        speak('good evening'+MASTER)

    print('please tell the question number\n')
    speak('please tell the question number')

def takeCommand():
    #query=input()
    
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:

        print('\n\nListening..say something: \n')
        speak('Recognizing...please speak')
        # use the default microphone as the audio source
        r.adjust_for_ambient_noise(source, duration=1) #wait for 10 seconds
        r.pause_threshold = 0.5
        audio = r.listen(source)

    
    try:
        query = r.recognize_google(audio,language='en-in') #langauge indian-english 
        print(f'\nYou said: {query}\n')

    except sr.RequestError:
        print("\nSorry, I can't access the Google API...\n") 
        speak("Sorry, I can't access the Google API...\n")  


    except sr.UnknownValueError:
        print("\nSorry, Unable to recognize your speech...\n")
        speak("\nSorry, Unable to recognize your speech...")
        query = None 

    
    return query
    


excel1 = wb.add_sheet('excel1')

def excel(i):
    while True:
       
        query=takeCommand()
        
        if 'exit' in query.lower() or 'bye' in query.lower() or 'quite' in query.lower():
            break

        else:
            j=0
            
            excel1.write(i, 0,query.lower())
           
            speak('please tell the marks')
            j+=1
            excel1.write(i,j,takeCommand())

excel(i