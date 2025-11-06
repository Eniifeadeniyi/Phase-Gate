import unittest
from functions import *

class TestStudentGradesApp(unittest.TestCase):
	def test_average_functions(self):
		actual = average(5,2)
		expected = 2.50
		self.assertEqual(actual,expected)

	def test_validate_function(self):
		actual = validate("5")
		expected = True
		self.assertEqual(actual,expected)
		actual = validate("5.75")
		expected = True
		self.assertEqual(actual,expected)
		actual = validate("5a75")
		expected = False
		self.assertEqual(actual,expected)
		actual = validate("110")
		expected = False
		self.assertEqual(actual,expected)
		actual = validate("-25")
		expected = False
		self.assertEqual(actual,expected)

	def test_maximum_function(self):
		actual = maximum([9,4,7,3])
		expected = 9
		self.assertEqual(actual,expected)

	def test_minimum_function(self):
		actual = minimum([9,4,7,3])
		expected = 3
		self.assertEqual(actual,expected)

	def test_descending_function(self):
		actual = descending([9,4,7,3])
		expected = [9,7,4,3]
		self.assertEqual(actual,expected)

	def test_edit_numbers(self):
		actual = edit_numbers([9,4,7,3],[9,7,4,3])
		expected =[1,3,2,4]
		self.assertEqual(actual,expected)
	
	