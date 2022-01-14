import pyttsx3  # text-to-speech conversion
import speech_recognition as sr   #convert speech to text
import datetime   #for fetching date and time
import wikipedia  # to search on wikipedia
import webbrowser  # to use browser and search things 
import smtplib  #SMTP client session object that can be used to send mail to any 
                #Internet machine with an SMTP or ESMTP listener daemon

import os    # to save/open files 
import playsound  # to play saved mp3 file
import time
import wordtodigits  # to convert spoken words into digits
import sys
import threading


sys.path.insert(0,'D:/python project/chatbot gui')
from app import ChatApplication,app,run


MASTER = 'shreyansh'
engine = pyttsx3.init('sapi5') #pyttsx3 module supports two voices first is female and the second 
                            #is male which is provided by “sapi5” for windows

voices = engine.getProperty('voices')
newVoiceRate = 145  # greater value = more speed 
engine.setProperty('rate',newVoiceRate)  #to make the voice go slower so that it can be easily understood
#engine.setProperty('voice', voices[0].id)


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
        
    print('\nI am shrey your desktop assistant....How may i help you ?\n')
    speak('I am shrey your desktop assistant....How may i help you ?')
# print((sr.Microphone.list_microphone_names()))


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:

        print('\n\nListening..say something: \n')
        speak('Recognizing...please speak')
        # use the default microphone as the audio source
        r.adjust_for_ambient_noise(source, duration=1) #wait for 10 seconds
        #r.pause_threshold = 0.5
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

wishme()


t=threading.Thread(target=ChatApplication) 
t.start()
app=ChatApplication()
app.run()

def tellDay():
    day = datetime.datetime.today().weekday()+1
      
    day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in day_dict.keys():
        day_of_the_week = day_dict[day]
        print('\n',day_of_the_week)
        speak("The day is " + day_of_the_week)


def wait():
    print('for how much time should i wait') 
    speak('for how much time should i wait') 
    a=takeCommand()
    a=(wordtodigits.convert(a)).lower() # converting the word into digits and then coverting the text into lower
    print(a)
    b=[int(i) for i in a.split() if i.isdigit()]  #taking the digits from the string into list
        
    if 'second' in a or 'seconds' in a:
        if b[0]==1:
            print(f'\nAlright...{MASTER} waiting for {b[0]} second\n')
            speak(f'Alright...{MASTER} waiting for {b[0]} second')
            time.sleep(b[0])

        else:
            print(f'\nAlright...{MASTER} waiting for {b[0]} seconds\n')
            speak(f'Alright...{MASTER} waiting for {b[0]} seconds')
            time.sleep(b[0])

    elif 'minute' in a or 'minutes' in a:
        c=b[0]*60
        if b[0]==1:
            print(f'\nAlright...{MASTER} waiting for {b[0]} minute\n')
            speak(f'Alright...{MASTER} waiting for {b[0]} minute')
            time.sleep(c)

        else:
            print(f'\nAlright...{MASTER} waiting for {b[0]} minutes\n')
            speak(f'Alright...{MASTER} waiting for {b[0]} minutes')
            time.sleep(c)

    elif 'hour' in a or 'hours' in a:
        c=b[0]*60*60
        if b[0]==1:
            print(f'\nAlright...{MASTER} waiting for {b[0]} hour\n')
            speak(f'Alright...{MASTER} waiting for {b[0]} hour')
            time.sleep(c)

        else:
            print(f'\nAlright...{MASTER} waiting for {b[0]} hours\n')
            speak(f'Alright...{MASTER} waiting for {b[0]} hours')
            time.sleep(c) 
            


while True:
    query=takeCommand()
    if 'wikipedia' in query.lower():
        print('\nSearching wikipedia...'+MASTER+' \n')
        speak('Searching wikipedia...'+MASTER)
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        print(f'\n{MASTER} do you want me to search on youtube?\n')
        speak(f'{MASTER} do you want me to search on youtube?')
        c=takeCommand()

        if 'you search' in c.lower() or 'yes' in c.lower() or 'sure' in c.lower():
            print("\nWhat do you want me to search for?\n")
            speak("What do you want me to search for?")
            k=takeCommand()

            if k != '':     # if "k" is not empty
                url = "https://www.youtube.com/results?search_query="+k
                print("\nHere are the search results for " + k+' \n')
                speak("Here are the search results for " + k)
                webbrowser.open(url)

            while(True):
                print(f'\n{MASTER} do you want anything else to search?\n')
                speak(f'{MASTER} do you want anything else to search?')
                a=takeCommand()

                if 'yes' in a.lower() or 'yeah' in a.lower() or 'sure' in a.lower():
                    print(f'\nAlright! {MASTER} what else you want me to search for?\n')
                    speak(f'Alright! {MASTER} what else you want me to search for?')
                    b=takeCommand()

                    if b!='':
                        url1 = "https://www.youtube.com/results?search_query="+b
                        print("\nHere are the search results for " + b+' \n')
                        speak("Here are the search results for " + b)
                        webbrowser.open(url1)

                    elif 'wait' in b.lower():
                        wait()    

                elif 'no' in a.lower() or 'nope' in a.lower() or 'leave' in a.lower() :
                    print(f'\nAlright! {MASTER} then what else i can do for you\n')
                    speak(f'Alright! {MASTER} then what else i can do for you')
                    break

                elif 'wait' in a.lower():
                    wait()

                else:
                    break

        elif 'no' in c.lower() or 'nope' in c.lower() or 'leave' in c.lower():
            print('\nAlright! just opening youtube...'+MASTER+' \n')
            speak('Alright! just opening youtube...'+MASTER)
            url = 'youtube.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)


    elif 'open google' in query.lower():
        print(f'\n{MASTER} do you want me to search on google?\n')
        speak(f'{MASTER} do you want me to search on google?')
        c=takeCommand()

        if 'you search' in c.lower() or 'yes' in c.lower():
            print("\nWhat do you want me to search for?\n")
            speak("What do you want me to search for?")
            k=takeCommand()

            if k != '':     # if "k" is not empty
                url ="https://google.com/search?q="+k
                print("\nHere are the search results for " + k+' \n')
                speak("Here are the search results for " + k)
                webbrowser.open(url)

            while(True):
                print(f'\n{MASTER} do you want anything else to search?\n')
                speak(f'{MASTER} do you want anything else to search?')
                a=takeCommand()

                if 'yes' in a.lower() or 'yeah' in a.lower() or 'sure' in a.lower():
                    print(f'\nAlright! {MASTER} what else you want me to search for?\n')
                    speak(f'Alright! {MASTER} what else you want me to search for?')
                    b=takeCommand()

                    if b!='':
                        url1 ="https://google.com/search?q="+k
                        print("\nHere are the search results for " + b+' \n')
                        speak("Here are the search results for " + b)
                        webbrowser.open(url1)

                    elif 'wait' in b.lower():
                        wait()    

                elif 'no' in a.lower() or 'nope' in a.lower() or 'sure' in a.lower():
                    print(f'\nAlright! {MASTER} then what else i can do for you\n')
                    speak(f'Alright! {MASTER} then what else i can do for you')
                    break

                elif 'wait' in a.lower():
                    wait()

                else:
                    break

        elif 'no' in c.lower() or 'nope' in c.lower() or 'leave' in c.lower(): 
            print('\nopening google...'+MASTER+' \n')       
            speak('opening google...'+MASTER)
            url = 'google.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open stackoverflow' in query.lower():
        print('\nopening stackoverflow...'+MASTER+' \n')
        speak('opening stackoverflow...'+MASTER)
        url = 'stackoverflow.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower():
        print('\nopening reddit...'+MASTER+' \n')
        speak('opening reddit...'+MASTER)
        url = 'reddit.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open facebook' in query.lower():
        print('\nopening facebook...'+MASTER+' \n')
        speak('opening facebook...'+MASTER)
        url = 'facebook.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open twitter' in query.lower():
        print('\nopening twitter...'+MASTER+' \n')
        speak('opening twitter...'+MASTER)
        url = 'twitter.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open instagram' in query.lower():
        print('\nopening instagram...'+MASTER+' \n')
        speak('opening instagram...'+MASTER)
        url = 'instagram.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open my github' in query.lower():
        print('\nopening your github account...'+MASTER+' \n')
        speak('opening your github account...'+MASTER)
        url = 'https://github.com/shreyansh-tyagi'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open github' in query.lower():
        print('\nopening github...'+MASTER+' \n')
        speak('opening github...'+MASTER)
        url = 'github.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open my hackerrank' in query.lower():
        print('\nopening your hackerrank account...'+MASTER+' \n')
        speak('opening your hackerrank account...'+MASTER)
        url = 'https://www.hackerrank.com/shreyansh_tyagi?hr_r=1'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open hackerrank' in query.lower():
        print('\nopening hacker rank...'+MASTER+' \n')
        speak('opening hacker rank...'+MASTER)
        url = 'hackerrank.com'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open sololearn' in query.lower():
        print('\nopening sololearn...'+MASTER+' \n')
        speak('opening sololearn...'+MASTER)
        url = 'https://www.sololearn.com/profile/20214219'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open my linkedin' in query.lower() or 'linkedin' in query.lower():
        print('\nopening your linkedin profile....'+MASTER+' \n') 
        speak('opening your linkedin profile....'+MASTER)   
        url='https://www.linkedin.com/in/shreyansh-tyagi-8577111a1/' 
        chrome_path='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\nthe time is {strTime}\n")
        speak('the time is '+strTime)

    elif 'date' in query.lower():
        strdate=datetime.datetime.now().strftime("%d %b %y") 
        print(f'\nthe date is {strdate}\n') 
        speak('the date is '+strdate)
         

    elif 'day' in query.lower():
        tellDay()     

    elif 'name' in query.lower():

        print('\nmy name is shrey...i am ready to help\n')
        speak('my name is shrey...i am ready to help')

    elif 'who are you' in query.lower() or 'introduce yourself' in query.lower():

        print('\ni am personal desktop assistant of mister' +MASTER+ 'who made me to help him out for completing his tasks\n') 

        speak('i am personal desktop assistant of mister' +MASTER+ 'who made me to help him out for completing his tasks') 
          

    elif 'how are you' in query.lower():
        print('\ni am fine....\n')
        speak('i am fine....'+MASTER)
        

    elif 'what can you do' in query.lower() or 'capablity' in query.lower():

        print('\ni am an application program that understands natural language voice commands and completes \
         tasks for my user.\n')


        speak('i am an application program that understands natural language voice commands and completes \
         tasks for my user.')

         
    elif 'job' in query.lower() or 'yourself' in query.lower():

        print('\ni can perform simple jobs for my users, such as adding tasks to a calendar, \
             providing information that would normally be searched in a web browser, \
             and receive phone calls, create text messages, get directions, hear news and weather reports, \
             hear music, or play games.\n')  


        speak('i can perform simple jobs for my users, such as adding tasks to a calendar, \
             providing information that would normally be searched in a web browser, \
             and receive phone calls, create text messages, get directions, hear news and weather reports, \
             hear music, or play games.') 


    elif 'nice' in query.lower() or 'good' in query.lower() or 'great' in query.lower():
        print('\nthank you....'+MASTER+' \n')  
        speak('ohh....thankyou '+MASTER)    


    elif 'search' in query.lower():
        print("\nWhat do you want me to search for?\n")
        speak("What do you want me to search for?")
        k=takeCommand()

        if k != '':     # if "k" is not empty
            url = "https://google.com/search?q="+k
            print("\nHere are the search results for " + k+' \n')
            speak("Here are the search results for " + k)
            webbrowser.open(url)

            while(True):
                print(f'\n{MASTER} do you want anything else to search?\n')
                speak(f'{MASTER} do you want anything else to search?')
                a=takeCommand()

                if 'yes' in a.lower() or 'yeah' in a.lower() or 'sure' in a.lower():
                    print(f'\nAlright {MASTER} what else you want me to search for?\n')
                    speak(f'Alright {MASTER} what else you want me to search for?')
                    b=takeCommand()

                    if b!='':
                        url1 = "https://google.com/search?q="+b
                        print("\nHere are the search results for " + b+' \n')
                        speak("Here are the search results for " + b)
                        webbrowser.open(url1)

                    elif 'wait' in b.lower():
                        wait()

                elif 'no' in a.lower() or 'nope' in a.lower() or 'leave' in a.lower():
                    print(f'\nAlright! {MASTER} then what else i can do for you\n')
                    speak(f'Alright! {MASTER} then what else i can do for you')
                    break

                elif 'wait' in a.lower():
                    wait()

                else:
                    break
                
    elif 'who made you' in query.lower() or 'owner' in query.lower():
        print(MASTER+'Tyagi')
        speak(MASTER+'Tyagi') 
        print(f'\ndo you want to know more about {MASTER}?\n')
        speak(f'do you want to know more about {MASTER}?')
        c=takeCommand()

        if 'yes' in c.lower() or 'sure' in c.lower() or 'yeah' in c.lower():

            print(f'\n{MASTER} is a MCA student from KIET group of institutions, who is right now developing me , he has \
            completed his BCA from CCS university , he have experience in using technologies like Python 3, \
             Numpy, Pandas, C, Data Structure in C, C++, HTML 5, CSS 3, GitHub ,Git bash \
            for version control and relational databases like my SQL, and Postgre SQL.\n')


            speak(f'{MASTER} is a MCA student from KIET group of institutions, who is right now developing me , he has \
            completed his BCA from CCS university , he have experience in using technologies like Python 3, \
             Numpy, Pandas, C, Data Structure in C, C++, HTML 5, CSS 3, GitHub ,Git bash \
            for version control and relational databases like my SQL, and Postgre SQL.')

            print(f"\nTo know more about {MASTER} check it out his github, hackerrank, linkedin profiles\n")
            speak(f"to know more about {MASTER} check it out his github, hackerrank, linkedin profiles")
            url='https://github.com/shreyansh-tyagi'
            url1='https://www.hackerrank.com/shreyansh_tyagi?hr_r=1'
            url2='https://www.linkedin.com/in/shreyansh-tyagi-8577111a1/'
            webbrowser.open(url)
            webbrowser.open(url1)
            webbrowser.open(url2)

        elif 'no' in c.lower() or 'nope' in c.lower() or 'leave' in c.lower():
            print(f'\nAlright! then what else i can do for you\n') 
            speak(f'Alright! then what else i can do for you')  

        else:
            print('\nunable to understand your voice\n')
            speak('unable to understand your voice')    


    elif f'introduce {MASTER}' in query.lower() or f'who is {MASTER}' in query.lower() or 'introduce' in query.lower():

        print(f'\n{MASTER} is a MCA student from KIET group of institutions, who is right now developing me , he has \
            completed his BCA from CCS university , he have experience in using technologies like Python 3, \
             Numpy, Pandas, C, Data Structure in C, C++, HTML 5, CSS 3, GitHub ,Git bash \
            for version control and relational databases like my SQL, and Postgre SQL.\n')

        speak(f'{MASTER} is a MCA student from KIET group of institutions, who is right now developing me , he has \
            completed his BCA from CCS university , he have experience in using technologies like Python 3, \
             Numpy, Pandas, C, Data Structure in C, C++, HTML 5, CSS 3, GitHub ,Git bash \
            for version control and relational databases like my SQL, and Postgre SQL.')

        print(f"\nto know more about {MASTER} check it out his github, hackerrank, linkedin profiles\n")  
        speak(f"to know more about {MASTER} check it out his github, hackerrank, linkedin profiles")
        url='https://github.com/shreyansh-tyagi'
        url1='https://www.hackerrank.com/shreyansh_tyagi?hr_r=1'
        url2='https://www.linkedin.com/in/shreyansh-tyagi-8577111a1/'
        webbrowser.open(url)
        webbrowser.open(url1)
        webbrowser.open(url2)


    elif 'wait' in query.lower():
        wait()
               
    elif 'i love you' in query.lower():
        print('\ni love you too' +MASTER+' \n')  
        speak('i love you too' +MASTER)           

    elif 'stop' in query.lower() or 'exit' in query.lower() or 'bye' in query.lower() or 'leave' in query.lower():
        print('\nokay bye, thanks for giving your time...'+MASTER+' \n')
        speak('okay bye, thanks for giving your time...'+MASTER)
        exit()


    else:
        print(f'\n{MASTER}, unable to understand what you are saying...trying to learn\n')
        speak(f'{MASTER}, unable to understand what you are saying...trying to learn')



    


      