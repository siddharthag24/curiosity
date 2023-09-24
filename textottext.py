#ENGLISH HINDI TEXT TRANSLATION 
from googletrans import Translator

def translate_to_hindi(text):
    try:        
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='hi')
        return translated_text.text

    except Exception as e:
        return str(e)

if _name_ == "_main_":
    english_text = "my name is manav"
    hindi_text = translate_to_hindi(english_text)

    print("English:", english_text)
    print("Hindi:", hindi_text)
