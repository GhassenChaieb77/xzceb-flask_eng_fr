import unittest
from translator import english_to_french, french_to_english
        
class TestTranslation(unittest.TestCase):
    def test_translation_null_input_englishToFrench(self):
        self.assertEqual(english_to_french(None), None)
        
    def test_translation_null_input_frenchToEnglish(self):
        self.assertEqual(french_to_english(None), None)
        
    def test_translation_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
    def test_translation_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

