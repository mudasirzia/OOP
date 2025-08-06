import speech_recognition as sr
import datetime as dt
import pyttsx3 as p
import webbrowser as wb
import os
import subprocess


class AI:

    def __init__(self):
        self.engine = p.init()

    def speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Jarvis is listening...")
            r.pause_threshold = 5  # Wait for user to stop speaking
            r.energy_threshold = 300  # Filter noise
            r.dynamic_energy_threshold = True

            try:
                # Keeps listening until user speaks
                audio = r.listen(source, timeout=None, phrase_time_limit=10)
                print("🤖 Processing your command...")
                command = r.recognize_google(audio)
                print(f"🗣️ You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speech("Sorry, I didn't catch that.")
                return ""
            except sr.RequestError:
                self.speech("Sorry, the speech service is down.")
                return ""

obj = AI()

def ExecuteAssistance():
    obj.speech("Hello, I am your personal AI assistant!")

    while True:
        command = obj.listen()

        # Define valid commands
        greetings = ["hello", "hi", "adaab", "acha", "jarvis", "mari shaboo"]
        google_cmds = [
            "google open karo",
            "jarvis open the google",
            "jarvis google kholo",
        ]
        whatsapp_cmds = [
            "jarvis whatsapp open karo",
            "open whatsapp",
            "jarvis whatsapp kholo",
        ]
        time_cmds = [
            "jarvis current time batao",
            "what is time by your watch?",
            "jarvis time kia hoa hai?",
            "time batao",
        ]
        exit_cmds = [
            "q",
            "exit",
            "jarvis band karo",
            "bass",
            "jarvis exit karo",
            "jarvis exit the program",
        ]
        cmd_cmds = ["jarvis open cmd", "jarvis cmd open karo"]

        try:
            # Response Conditions
            if command in greetings:
                obj.speech("Hello! Nice to meet you!")

            elif command in google_cmds:
                obj.speech("Opening Google...")
                wb.open("https://www.google.com")

            elif command in whatsapp_cmds:
                obj.speech("Opening WhatsApp...")
                os.system("start whatsapp:")

            elif command in cmd_cmds:
                obj.speech("Opening Command Prompt...")
                # ✅ Fixed: CMD now opens properly using `start` on Windows
                subprocess.Popen("start cmd", shell=True)

            elif command in time_cmds:
                ct = dt.datetime.now()
                lct = ct.strftime("%I:%M:%S %p")
                obj.speech(f"Current time is {lct}")

            elif command in exit_cmds:
                obj.speech("Exiting... Goodbye!")
                break

            elif command != "":
                obj.speech("I didn't understand that. Try again.")

        except Exception as e:
            obj.speech(f"An error occurred: {e}")

if __name__ == "__main__":
    ExecuteAssistance()
