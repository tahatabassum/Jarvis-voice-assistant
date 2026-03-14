import speech_recognition as sr
import pyttsx3
import webbrowser
from special_sites import special_sites
import time


# Initialize recognizer and TTS
r = sr.Recognizer()
r.energy_threshold = 300  # adjust to ambient noise

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
engine.setProperty('rate', 180)


# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()




# Play YouTube song (lazy import pywhatkit)

def play_song(song_name):
    speak(f"Searching {song_name} on YouTube")
    # Open search results immediately in browser
    query = song_name.replace(" ", "+")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    
    # Lazy import pywhatkit to play first YouTube result
    time.sleep(5)  # wait a bit so browser loads
    try:
        import pywhatkit
        pywhatkit.playonyt(song_name)
    except Exception as e:
        speak("Sorry, I could not play the song.")
        print("Error:", e)



# Process commands
def processcommands(command):
    command = command.lower().strip()
    # Open special sites 
    if "open" in command:
        site_name = command.replace("open ", "").strip()
        if site_name in special_sites:
            url = special_sites[site_name]
            speak(f"Opening {site_name}")
            webbrowser.open(url)
        else:
            speak(f"Sorry, I don't have {site_name} in my list")

    #Play YouTube songs
    elif command.startswith("play"):
        song_name = command.replace("play ", "").strip()
        play_song(song_name)

    #Stop listening / exit
    elif "goodbye" in command and "jarvis" in command:
        speak("Goodbye boss! Shutting down.")
        return False

    else:
        speak("Sorry, I can't understand you")

    return True  # continue listening



# Main program
active = False  # wake word not detected yet

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")

    while True:
        try:
            audio = r.listen(source)
            word = r.recognize_google(audio)
            print("Heard:", word)

            if not active:
                # Wake word detection
                if "jarvis" in word.lower():
                    active = True
                    speak("Yes boss, I am listening")
                    print("Jarvis activated")
            else:
                # Process commands
                active = processcommands(word)
                if active is False:
                    break  # EXIT THE LOOP → stops listening

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Speech service unavailable")

        except Exception as e:
            print("Error:", e)