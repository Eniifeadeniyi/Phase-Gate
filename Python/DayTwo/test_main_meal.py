import unittest
from main_meal import *

class TestMainMeal(unittest.TestCase):
	def test_that_make_new_word_works(self):
		actual = make_new_word("abcdefd", "d")
		expected = "dcbaefd"
		self.assertEqual(actual,expected)
		actual = make_new_word("abcef","d")
		expected = "abcef"
		self.assertEqual(actual,expected)

	def test_that_make_new_word_only_takes_in_letters_for_word_parameter(self):
		actual = make_new_word("1","d")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = make_new_word(1,"d")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = make_new_word(4.5,"d")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)


	def test_that_make_new_word_only_takes_in_letters_for_ch_parameter(self):
		actual = make_new_word("d","1")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = make_new_word("d", 1)
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = make_new_word("d", 4.5)
		expected = "Invalid input!"
		self.assertEqual(actual,expected)



		