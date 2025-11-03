import unittest
from checkout_system_functions import *

class TestCheckoutSystem(unittest.TestCase):
	def test_that_make_invoice_works(self):
		actual = make_invoice("Laptop",30000)
		expected = {"Laptop" : 30000,}
		self.assertEqual(actual,expected)

	def test_that_make_invoice_only_takes_in_int_for_price(self):
		actual = make_invoice("Laptop","laptop")
		expected = {}
		self.assertEqual(actual,expected)

	def test_that_make_invoice_does_not_take_negative_numbers(self):
		actual = make_invoice("Laptop",-500)
		expected = {}
		self.assertEqual(actual,expected)

	def test_that_get_sum_works(self):
		actual = get_sum({"Laptop": 30000, "Apple" : 30000, "Book" : 5000})
		expected = 65000
		self.assertEqual(actual,expected)
	
	def test_that_get_vat_works(self):
		actual = get_vat(65000)
		expected = 4875
		self.assertEqual(actual,expected)

	def test_that_get_total_works(self):
		actual = get_total(65000,4875)
		expected = 69875
		self.assertEqual(actual,expected)

	def test_that_edit_invoice_works(self):
		invoice = {"Laptop": 30000, "Apple" : 30000, "Book" : 5000}
		actual = edit_invoice(65000,4875,69875,invoice)
		expected = {"Laptop": 30000, "Apple" : 30000, "Book" : 5000, "Subtotal" : 65000, "VAT" : 4875, "Total Amount" : 69875,}
		self.assertEqual(actual,expected)


	def test_that_check_payment_works(self):
		actual = check_payment(50000,65000)
		expected = 50000
		self.assertEqual(actual,expected)

	def test_that_check_payment_only_takes_whole_number_int(self):
		actual = check_payment("fifty", 65000)
		expected = "Invalid input!"
		self.assertEqual(actual,expected)
		actual = check_payment(-65000, 65000)
		expected = "Invalid input!"
		self.assertEqual(actual,expected)

	def test_that_check_payment_only_takes_needed_amount(self):
		actual = check_payment(70000,65000)
		expected = "Overpay!"
		self.assertEqual(actual,expected)

	def test_that_get_balance_works(self):
		actual = get_balance(65000,60000)
		expected = 5000
		self.assertEqual(actual,expected)

	def test_that_make_receipt_works(self):
		actual = make_receipt("Laptop", 30000)
		expected = {"Laptop" : 30000,}
		self.assertEqual(actual,expected)

	def test_that_make_receipt_only_takes_in_int_for_price(self):
		actual = make_receipt("Laptop","laptop")
		expected = {}
		self.assertEqual(actual,expected)

	def test_that_make_receipt_does_not_take_negative_numbers(self):
		actual = make_receipt("Laptop",-500)
		expected = {}
		self.assertEqual(actual,expected)

	def test_that_edit_receipt_works(self):
		actual = edit_receipt(65000,5000,60000,{"Laptop" : 65000})
		expected = {"Laptop" : 65000, "Total Paid" : 60000, "Grand Total" : 65000, "Balance" : 5000}
		self.assertEqual(actual,expected)

