
# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
from jokes import randJk

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    text = r.recognize_sphinx(audio, language = "fr-FR")
    print(text)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))


if text == "histoire drôle":
    blague = "Il était une fois...\nAh! pis d'la marde!"

    import pyttsx3
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')[1] # the french voice

    engine.setProperty('voice', voice.id)
    joke = randJk()
    print(joke)

    engine.say(joke) # perfect # it works!!

    engine.runAndWait()
