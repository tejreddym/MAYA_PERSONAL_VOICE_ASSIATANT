#pip install google-generativeai
#pip install pyttsx3
#pip install SpeechRecognition
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak_response(response):
    engine.say(response)
    engine.runAndWait()

genai.configure(api_key="Enter-Your-API-Key")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[{"role": "user", "parts": "Hello"},
                                 {"role": "model", "parts": " MAYA, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks 1  as best I can, 24 hours a day, 7 days a week. Importing all preferences from home interface. Systems are now fully operational."},])
def maya(query):
    response = chat.send_message(query, stream=True)
    for chunk in response:
        a = chunk.text
        print(a)
        speak_response(a)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=7)
            
            # Recognize speech directly (no noise reduction)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""
        
print("Allow me to introduce myself. I am MAYA, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks 1  as best I can, 24 hours a day, 7 days a week. Importing all preferences from home interface. Systems are now fully operational.")
speak_response("Allow me to introduce myself. I am MAYA, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks 1  as best I can, 24 hours a day, 7 days a week. Importing all preferences from home interface. Systems are now fully operational.")
while True:
    query = listen()
    maya(query)