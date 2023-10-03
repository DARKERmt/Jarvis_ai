import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def call():
    audio = r.listen(source)
    print("Recognizing...")
    query = r.recognize_google(audio, language='en')
    print(f"User said: {query}\n")

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your JARVIS. How can I assist you today?")

# Function to listen to user's command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you please repeat?")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "None"

# Function to execute user's command
def execute_command(command):
    if 'jarvis' in command:
        speak('Searching...')
        command = command.replace("jarvis", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
    elif 'play music' in command:
        music_dir = 'C:\\Music'  # Replace with your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found in the directory.")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    elif 'who are you' in command:
        speak("My name is Jarvis. I am a virtual assistant created by Praveen.")
    elif "who is Praveen" in command:
        speak("Praveen is my owner.")
    else:
        speak("Sorry, I am not programmed to perform that task.")

# Main program loop
if __name__ == "__main__":
    greet()
    while True:
        command = listen()
        execute_command(command)
