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

  

#text to text 
from googletrans import Translator

def translate_to_hindi(text):
    try:
        # Create a Translator object
        translator = Translator()

        # Translate the text to Hindi
        translated_text = translator.translate(text, src='en', dest='hi')

        # Return the translated text
        return translated_text.text

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Input English text
    english_text = "my name is manav"

    # Translate the text to Hindi
    hindi_text = translate_to_hindi(english_text)

    # Print the translated text
    print("English:", english_text)
    print("Hindi:", hindi_text)
