import pyttsx3
import sounddevice as sd
import numpy
import speech_recognition as sr
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def litsen():
    print("Listening for 5 seconds!")
    fs = 44100
    seconds = 5
    print("Speak now")
    recording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1, dtype = 'int16')
    sd.wait()
    audio_bytes = recording.tobytes()

    r = sr.Recognizer()
    audio_data = sr.AudioData(audio_bytes, fs, 2)

    try:
        text = r.recognize_google(audio_data)
        print(f"You said {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry! i dont catch that!!")
        return ""

def main():
    speak("Hello iam your assistand!How can i help you?")
    while True:
        command = litsen()
        if command == "":
            continue
        if "quit" in command or "exit" in command:
            speak("goodbye!")
            break 
        elif "hello" in command or "hi" in command:
            speak("HI. How can i help you?")
        else:
            speak("Sorry! I didnt understand that command")
main()
