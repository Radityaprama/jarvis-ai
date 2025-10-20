import pyttsx3
import speech_recognition as sr
import random
import time

# text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175) 

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-US')
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you repeat?")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

def jarvis_reply(command):
    responses = {
        "hello": ["Hello, boss!", "Hey there!", "Hi, nice to see you!"],
        "how are you": ["I'm great, thank you!", "Doing awesome as always!", "I'm feeling fantastic today!"],
        "what time is it": [f"The time is {time.strftime('%I:%M %p')}"],
        "bye": ["Goodbye!", "See you later!", "Powering down. Have a nice day!"]
    }

    for key, val in responses.items():
        if key in command:
            return random.choice(val)

    return "I'm sorry, I don't understand that yet."

# main program
if __name__ == "__main__":
    speak("Hello! I'm Jarvis, your offline assistant.")
    while True:
        command = listen()
        if not command:
            continue
        if "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Shutting down.")
            break
        reply = jarvis_reply(command)
        speak(reply)
