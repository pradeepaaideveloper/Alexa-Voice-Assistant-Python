import speech_recognition as sr
import pyttsx3 #speach to text
import pywhatkit # online platform asscess
import datetime
import wikipedia
import pyjokes
import sys

listener =sr.Recongnizer()
engine=ppyttsx3.init()

voice = engine.getProperty('voices')

if len(voices)>1:
    engine.setProperty('voices',voice[1].id)
else:
    engine.setProperty('voices',voice[0].id)

def engine_talk(text):
    print(f"Alexa is saying:{text}")
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone()as soutce:
            listner.adjust_for_ambient_noise(source)
            print("Start Speaking!!")
            voice+listner.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(f"User said:{command}")
                return command
    except Exception as e:
        print(f"Error:{e}")
        return""
def run_alexa():
    command = user_commands()
    if command:
        if'play' in command:
            song = command.replace('play','')
            engine_talk('Playing'+song)
            pywhatkit.playonyt(song)
        elif'time' in command:
            time = datetime.datetime.now.strftime('%I:%M:%p')
            engine_talk("The Current time is"+time)
        elif'who is' in command:
            name = command.replace('who is','')
            info=wikipedia.summary(name,1)
            print(info)
            engine_talk(info)
        elif'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif'stop' in demamnd:
            sys.exit()
        else:
            engine_talk("I could not hear you properly")
    else:
        engine_talk("I did not catch that.Please again")
while True:
    run_alexa()
