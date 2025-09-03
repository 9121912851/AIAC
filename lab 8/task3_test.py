import unittest
from task3 import is_sentence_palindrome

class TestIsSentencePalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_sentence_palindrome("madam"))
        self.assertTrue(is_sentence_palindrome("racecar"))
        self.assertTrue(is_sentence_palindrome("A"))
        self.assertTrue(is_sentence_palindrome(""))

    def test_sentence_palindrome_with_spaces(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))

    def test_sentence_palindrome_with_punctuation(self):
        self.assertTrue(is_sentence_palindrome("Madam, in Eden, I'm Adam."))
        self.assertTrue(is_sentence_palindrome("Eva, can I see bees in a cave?"))
        self.assertTrue(is_sentence_palindrome("Able was I, ere I saw Elba!"))

    def test_non_palindrome_sentences(self):
        self.assertFalse(is_sentence_palindrome("Hello, world!"))
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
        self.assertFalse(is_sentence_palindrome("Palindrome"))

    def test_mixed_case_and_numbers(self):
        self.assertTrue(is_sentence_palindrome("1A2b2A1"))
        self.assertTrue(is_sentence_palindrome("12321"))
        self.assertFalse(is_sentence_palindrome("12345"))

    def test_only_non_alphanumeric(self):
        self.assertTrue(is_sentence_palindrome("!!!"))
        self.assertTrue(is_sentence_palindrome("   "))
        self.assertTrue(is_sentence_palindrome("...,,,;;;"))

    def test_unicode_characters(self):
        self.assertTrue(is_sentence_palindrome("А роза упала на лапу Азора"))  # Cyrillic palindrome
        self.assertFalse(is_sentence_palindrome("こんにちは"))  # Not a palindrome

if __name__ == '__main__':
    unittest.main()
