import speech_recognition as sr
import pyttsx3



r=sr.Recognizer()
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
mic = sr.Microphone()
r.energy_threshold=1500

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with mic as source:
        
            print("Give Input:",end=" ")
            r.adjust_for_ambient_noise(source)
            voice=r.listen(source)
            command= r.recognize_google(voice,language='en-US',key=None)
        command = command.lower()
        if 'alexa' in command:
            command=command.replace("alexa","")
            print(command)
    except:
        command="NO COMMAND GIVEN"
    return command
def run_alexa():
    # song = AudioSegment.from_wav("Siri Open.wav")
    # play(song)
    command=take_command()
    print(command)
    return command
while True:   
    run_alexa()
    print()