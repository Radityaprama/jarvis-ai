import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print("=== Available voices ===")
for i, v in enumerate(voices):
    print(f"{i}: {v.name} ({v.id})")

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
engine.say("Hello! This is a voice test.")
engine.runAndWait()
