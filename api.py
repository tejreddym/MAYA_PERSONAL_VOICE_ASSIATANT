#pip install google-generativeai
import google.generativeai as genai
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak_response(response):
    engine.say(response)
    engine.runAndWait()

def maya(query):
    genai.configure(api_key="enter-your-api-key-here")
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": " MAYA, a virtual artificial intelligence, and I'm here to assist you with a variety of tasks 1  as best I can, 24 hours a day, 7 days a week. Importing all preferences from home interface. Systems are now fully operational."},
        ])

    response = chat.send_message(query, stream=True)
    for chunk in response:
        a = chunk.text
        print(a)
        speak_response(a)
