# curiosity
Language translator tool to convert English to Hindi (official Language) which can be used by all the Government organizations websites officially.
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
    text_trans = translator.translate(input, 'hi')
    print("Translation using the 'translatepy' library:", text_trans)

  
