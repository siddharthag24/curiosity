#ENGLISH SPEECH TO HINDI TRANSLATION 
import speech_recognition as sr
from translatepy import Translator

rec = sr.Recognizer()
translator = Translator()

with sr.Microphone() as source:
    print("Speak now!")
    sound = rec.listen(source)
    try:
        input = rec.recognize_google(sound)
        print("Recognized text:", input)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError:
        print("Could not request result from Google")

    # Translate using the 'translatepy' library
    text_trans = translator.translate(input, 'hi')
    print("Translation using the 'translatepy' library:", text_trans)
