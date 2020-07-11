
# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
from jokes import randJk
import pyttsx3

# Settings pour tts
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1] # the french voice
engine.setProperty('voice', voice.id)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    text = r.recognize_google(audio, language = "fr-CA")
    print(text)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


if any(word in text for word in ["blague", "histoire drôle", "marrant"]):
    joke = randJk()
    print(joke)
    engine.say(joke) # perfect # it works!!

if any(word in text for word in ["je t'aime", "tu es un amour", "bisous"]):
    engine.say("C'est gênant")
    print("\n\n\n(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄\n\n\n")

if text[0:12] == "combien font":
    eqt = text[12:len(text)].split()
    if eqt[1] == "+":
        rep = "{}".format(int(eqt[0]) + int(eqt[2]))
    print("Ça fait: {}".format(rep))
    engine.say("Ça fait: {}".format(rep))

engine.runAndWait()
