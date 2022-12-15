""" This module tests French and English translation """
import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    """
    This class translates french to english
    """
    def test_equal(self):
        """
        This function translates french to english assert equal
        """
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')  # test Au revoir.

    def test_not_equal(self):
        """
        This function translates french to english assert not equal
        """
        self.assertNotEqual(french_to_english('None'), '')  # test for null.

class TestEnglishToFrench(unittest.TestCase):
    """
    This class translates english to french
    """
    def test_equal(self):
        """
        This function translates english to french assert equal
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test Hello.

    def test_not_equal(self):
        """
        This function translates english to french assert not equal
        """
        self.assertNotEqual(english_to_french('None'), '') # test for null.

if __name__ == '__main__':
    unittest.main(verbosity=2)
