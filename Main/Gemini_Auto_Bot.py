#Initial System Ask
import pyttsx3
import google.generativeai as genai
import os
#LIstening from user and typing
import speech_recognition as sr


def text_to_speech1(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 95) 
    engine.setProperty('volume', 1.0) 
    engine.setProperty('voice', voices[1].id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

text = "I am listening to you, please speak something"
text_to_speech1(text)

# Initialize recognizer
recognizer = sr.Recognizer()


def listen_and_convert():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Convert speech to text
            print("Converting speech to text...")
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Error connecting to the speech recognition service.")
    
# Run the speech-to-text function
user_text = listen_and_convert()

#API

def generate_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while generating the response: {e}")
        return None

if __name__ == "__main__":
     api_key = os.environ['GOOGLE_API_KEY']
     genai.configure(api_key=api_key)
  
    # Get the response from Gemini
     response = generate_response(user_text)

     if response:
        print("Gemini API Response:")
        print(response)
     else:
        print("No response received.")



def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init() 
    # Set properties (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 1.0)
    engine.setProperty('voice', voices[1].id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

text_to_speech(response)


def repeat_speech_if_needed(text):
    while True:
        # Ask the user if they understood
        text_to_speech1("Did you understand the message")
        user_input = input("Did you understand the message? (yes/no): ").strip().lower()
        
        
        # Check user response
        if user_input == 'yes':
            print("Great! Moving on.")
            text_to_speech1("Great! Moving on.")
            break  
        elif user_input == 'no':
            print("Repeating the message...")
            # Convert text to speech
            text_to_speech(text)
        else:
            print("Please respond with 'yes' or 'no'.")

# Run the repeat_speech_if_needed function
repeat_speech_if_needed(response)

