# Commands of J.A.R.V.I.S are -

# It can greet us when it is good morning it says morning and when it is afternoon it will say afternoon and when it is night it will say night.
# It can take our commands and when we do not say anything it does not takes our commands.
# It can turn on camera when we our in any meeting.
# It can search anything on wikipedia.
# It can open youtube , amazon , citibank , discord , whatsapp , python , zoom , skype , lichess , google , flipkart.
# It can play any video or any music on youtube.
# It can tell you the current time.
# It can tell you jokes.
# It can quit whenever we say quit.
# It can tell who he is.
# It can tell answers to questions like hello and fine.
# It can shutdown automatically.
# It can show news.
# It can tell you weather forcast.
# It can restart system.
# It can log out from the system.
# It can set timer.

print("To run the jarvis first you have to wait till when you don't get the word listening and then you have to say the commands that are writen in quotes and then it will run.")







import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import pyjokes
import cv2 # releated to files.
import winsound
#import python_weather
import datetime
from playsound import playsound
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir , what can I do for you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


        
def SecurityCamera():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret,frame1 = cam.read()
        ret,frame2 = cam.read()
        diff = cv2.absdiff(frame1 , frame2)
        gray = cv2.cvtColor(diff , cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh , None , iterations=3)
        contours, _ = cv2.findContours(dilated , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1 , contours, -1 , (0 , 255 , 0) , 2)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame1 , (x , y) , (x + w , y + h) , (0 , 255 , 0) , 2)
            winsound.Beep(500,100)
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Dakshit cam' , frame1)

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True 
    while(result): 
        #read the frames while the camera is on 
        ret,frame = videoCaptureObject.read() 
        #cv2.imwrite() method is used to save an image to any storage device 
        cv2.imwrite("C:/Users/Dakshit/Desktop/main folder/whitehat jr/camera/NewPicture1.jpg",frame) 
        result = False

     # releases the camera 
    videoCaptureObject.release() 
    #closes all the window that might be opened while this process 
    cv2.destroyAllWindows() 

# take_snapshot()        


if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
            

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'snapshot' in query:
            take_snapshot()

        elif 'hello' in query:
            speak("Hello sir How are you ")

        elif 'fine' in query:
            speak("that great sir please tell me what can I do for you")
        elif 'who are you' in query:
            speak("I am Jarvis and I am a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe.")

          

        elif 'play' in query:
            whatShouldPlay = query.replace('play', '')
            speak('playing ' + whatShouldPlay)
            pywhatkit.playonyt(whatShouldPlay)


         

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            speak("Bye Sir Have A Nice Day.")
            speak("If You Want More Help Please call Me Again.")
            speak("Thank You Sir")
            exit()

        elif 'camera' in query:
            SecurityCamera()

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")

        elif 'open citibank' in query:
            webbrowser.open(".citibank.co.in/ibank/login/IQPin1.jsp?dOfferCode=PAYCCBILL")

        elif 'open discord' in query:
            webbrowser.open("https://discord.com/channels/777879401990717470/777879401990717473")

        elif 'open whatsapp' in query :
            codePath = "https://web.whatsapp.com/"
            os.startfile(codePath)

        elif 'open zoom' in query :
            codePath = "https://zoom.us/"
            os.startfile(codePath)

        elif 'open python' in query :
            codePath = "https://www.python.org/"
            os.startfile(codePath)
        elif 'open skype' in query :
            codePath = "https://www.skype.com/en/"
            os.startfile(codePath)

        elif 'open lichess' in query :
            codePath = "https://lichess.org/"
            os.startfile(codePath)

        elif 'open google' in query :
            codePath = "https://www.google.com/"
            os.startfile(codePath)

        elif 'open flipkart' in query :
            codePath = "https://www.flipkart.com/"
            os.startfile(codePath)

        elif 'shutdown' in query:
            speak("Do you really want to shutdown your sysytem sir ?")
            relpy = takeCommand().lower()
            if 'yes' in relpy:
                os.system('shutdown /s /t 1')
            else:
                speak("As you wish sir ! ")

        elif 'show news' in query:
            speak("Here are some top headlines ")
            webbrowser.open("https://news.google.com/")

        elif 'what is the weather today' in query:
            speak("Weather for differnt cites today is") 
            #relpy = takeCommand().lower()
            #country = relpy
            webbrowser.open("https://www.ndtv.com/weather")

         
                     
        elif 'restart' in query:
            speak("Do you really want to restart your sysytem sir ?")
            relpy = takeCommand().lower()
            if 'yes' in relpy:
                os.system('shutdown /r /t 1')
            else:
                speak("As you wish sir ! ")


        elif 'log out' in query:
            speak("Do you really want to log out your sysytem sir ?")
            relpy = takeCommand().lower()
            if 'yes' in relpy:
                os.system('shutdown -1')
            else:
                speak("As you wish sir ! ")



        elif 'timer' in query:
            speak("How many seconds to wait ")
            seconds = int(input("How many seconds to wait ? "))

            for i in range(seconds):
                print(str(seconds - i) + " seconds remain ")
                time.sleep(0.1)
