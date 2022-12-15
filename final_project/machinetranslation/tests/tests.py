""" This module tests French and English translation """
import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    This class translates english to french
    """
    def test1(self):
        """
        This function translates english to french
        """
        self.assertNotEqual(english_to_french('None'), '') # test for null.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test Hello.
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')  # test Goodbye.

class TestFrenchToEnglish(unittest.TestCase):
    """
    This class translates french to english
    """
    def test1(self):
        """
        This function translates french to english
        """
        self.assertNotEqual(french_to_english('None'), '') # test for null.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test Bonjour.
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')  # test Au revoir.

unittest.main()
