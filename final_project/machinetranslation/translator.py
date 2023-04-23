import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# Load credentials from .env file
apikey = os.environ['TRANSLATOR_APIKEY']
url = os.environ['TRANSLATOR_URL']

# Create language translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(text):
    """
    Translates English text to French
    """
    if text:
        translation = language_translator.translate(
            text=text,
            source='en',
            target='fr'
        ).get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    return ""

def french_to_english(text):
    """
    Translates French text to English
    """
    if text:
        translation = language_translator.translate(
            text=text,
            source='fr',
            target='en'
        ).get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    return "" 
