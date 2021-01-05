import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening!")

def takeCommand(question=None):
    if(question != None):
        speak(question)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("You said: ", query)

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    speak("I am your desktop assistant, JARVIS(Just A Rather Very Intelligent System). How may I help you ?")
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            query = takeCommand("Whatshould I search on wikipedia? ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Ok, opening YouTube")
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            speak("Ok, opening Google")
            webbrowser.open('https://www.google.co.in/')

        elif 'open stack overflow' in query:
            speak("Ok, opening stack overflow")
            webbrowser.open('https://stackoverflow.com/')

        elif 'open amazon' in query:
            speak("Ok, opening amazon")
            webbrowser.open('https://www.amazon.in/ref=nav_logo')

        elif 'open gmail' in query:
            speak("Ok, opening your G-Mail")
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
