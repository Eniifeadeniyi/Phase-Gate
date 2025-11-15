import unittest
from functions_two import *

class TestFunctions(unittest.TestCase):
	def test_that_collect_names_works(self):
		actual = collect_names("Elena")
		expected = ["Elena"]
		self.assertEqual(actual,expected)
		names = ["elena"]
		actual = collect_names("Elena")
		expected = ["Elena"]
		self.assertEqual(actual,expected)
		actual = collect_names("56")
		expected = ["Elena"]
		self.assertEqual(actual,expected)