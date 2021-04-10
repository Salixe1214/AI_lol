
# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
from jokes import randJk
import pyttsx3

# Settings pour tts
engine = pyttsx3.init()
voices = engine.getProperty('voices')
v_id = voices[0].id
for voice in voices:
    if 'French' in voice.name:
        v_id = voice.id

engine.setProperty('voice', v_id)

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
    print("\n\n\n(/ /*/w/*/ /)/\n\n\n")

if text[0:12] == "combien font" and len(text[12:len(text)].split()) == 3:
    eqt = text[12:len(text)].split()
    if eqt[1] == "+":
        rep = "{}".format(float(eqt[0]) + float(eqt[2]))
    print("Ça fait: {}".format(rep))
    engine.say("Ça fait: {}".format(rep))

if any(word in text for word in ["aide", "que peux-tu faire", "fonctionnalités", "fonctionnalité",
                                 "fonctionnalitée", "fonctionnalitées"]):
    phrase = "Je peux:\n"
    phrase = phrase + "Raconter une blague\n"
    phrase = phrase + "Faire une addition binaire\n"
    phrase = phrase + "Lister mes fonctionnalités\n"

# if any(word in text for word in ["roche, papier, ciseau", "shifumi"]):
#     """
#     # TODO: Faire un jeu de roche-papier-sciseau.
#     """
#     skip

engine.runAndWait()
