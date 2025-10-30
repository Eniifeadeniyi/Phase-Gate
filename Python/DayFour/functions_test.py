import unittest
from functions import *

class TestFunctions(unittest.TestCase):
	def test_that_get_perfect_square_works(self):
		actual = get_perfect_square([25,49,9,4,2])
		expected = [True, True, True, True, False]
		self.assertEqual(actual,expected)
		
	def test_that_get_perfect_square_takes_in_only_int(self):
		actual = get_perfect_square([4,9,25,49,-5.2])
		expected = [True, True, True, True, "Invalid!"]
		self.assertEqual(actual,expected)

	def test_that_get_palindrome_flags_works(self):
		actual = get_palindrome_flags(["madam",5,"word"])
		expected = [True, True, False,]
		self.assertEqual(actual,expected)