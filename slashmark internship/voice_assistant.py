import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens for a voice command and returns it as text"""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Reduce noise
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Network error.")
        return None

if __name__ == "__main__":

    speak("How can I assist you?")
    while True:
        command = take_command()
        
        if command:
            if "hello" in command:
                speak("Hello! How can I help you today?")
            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I can only respond to basic commands.")