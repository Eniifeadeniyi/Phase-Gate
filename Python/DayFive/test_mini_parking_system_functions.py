import unittest
from mini_parking_system_functions import *

class TestMiniParkingSystem(unittest.TestCase) :
	def test_that_park_works(self):
		actual = park([0,1,2,3],2)
		expected = [0,1,3]
		self.assertEqual(actual,expected)
		actual = park([0,1,2,3],"2")
		expected = [0,1,3]
		self.assertEqual(actual,expected)

	def test_that_you_can_only_park_in_available_spaces(self):
		actual = park([0,1,2,3],5)
		expected = "Unavailable!"
		self.assertEqual(actual,expected)

	def test_that_park_only_takes_in_int(self):
		actual = park([0,1,2,3],"five")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = park([0,1,2,3],-2.5)
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
	
	def test_that_change_cars_works(self):
		actual = change_cars([0,1,2,3],[0,0,0,0],2)
		expected = [0,0,1,0]
		self.assertEqual(actual,expected)
		actual = change_cars([0,1,2,3],[0,0,0,0],"2")
		expected = [0,0,1,0]
		self.assertEqual(actual,expected)

	def test_that_update_occupied_works(self):
		actual = update_occupied([],19)
		expected = [19]
		self.assertEqual(actual,expected)
		actual = update_occupied([],"19")
		expected = [19]
		self.assertEqual(actual,expected)

	def test_that_update_spaces_works(self):
		actual = update_spaces([],1)
		expected = [1]
		self.assertEqual(actual,expected)
		actual = update_spaces([],"1")
		expected = [1]
		self.assertEqual(actual,expected)

	def test_that_unpark_works(self):
		actual = unpark([19],19)
		expected = []
		self.assertEqual(actual,expected)
		actual = unpark([19],"19")
		expected = []
		self.assertEqual(actual,expected)

	def test_that_you_can_not_unpark_a_car_not_parked(self):
		actual = unpark([],19)
		expected = "Car not found!"
		self.assertEqual(actual,expected)

	def test_that_unpark_only_takes_in_int(self):
		actual = unpark([1,0,18],"five")
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = unpark([1,0,18],-2.5)
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
	
	def test_reverse_cars_works(self):	
		actual = reverse_cars([0,0,1,0],2)
		expected = [0,0,0,0]
		self.assertEqual(actual,expected)
		actual = reverse_cars([0,0,1,0],"2")
		expected = [0,0,0,0]
		self.assertEqual(actual,expected)


	


	