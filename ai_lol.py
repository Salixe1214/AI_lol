#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source
# listening the audio file and store in audio_text variable


with sr.Microphone() as source:
    x = 0
    while x < 5:

        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            text = r.recognize_sphinx(audio_text)
            print(text)

        except:
             print('Sorry.. run again...')

        x = x + 1
