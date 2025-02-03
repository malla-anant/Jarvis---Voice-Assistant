import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests 

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "212581f597b84303bb704d907a17d356"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
        if r.status_code == 200:
            #paste the JSON response
            data = r.json()

            #Extract the articals
            articles = data.get('articles', [])

            #print the headline
            for article in articles:
                speak(article['title'])

if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        #Lisen for the wake word  "jarvis"
        #obain audio from the microphone 
        r = sr.Recognizer()
        

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("hello anant, how can i help you...")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e)) 