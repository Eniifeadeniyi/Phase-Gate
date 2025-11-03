invoice = {}
receipt = {}
def make_invoice(product_name,product_price):
	if type(product_price) == float or type(product_price) == int:
		if product_price >= 0:
			invoice[product_name] = product_price

	return invoice

def get_sum(invoice):
	subtotal = sum(invoice.values())
	return subtotal

def get_vat(subtotal):
	vat = subtotal * 0.075 
	return vat
		
def get_total(subtotal,vat):
	total = subtotal + vat
	return total

def edit_invoice(subtotal, vat, total, invoice):
	invoice["Subtotal"] = subtotal
	invoice["VAT"] = vat
	invoice["Total Amount"] = total
	return invoice

def check_payment(payment,total):
	if type(payment) == float or type(payment) == int:
		if payment < -1:
			return ("Invalid input!")
		if payment <= total and payment:
			return float(payment)
		else:
			return ("Overpay!")
	else:
		return ("Invalid input!")

def get_balance(total,payment):
	balance = total - payment
	return balance

def make_receipt(product_name,product_price):
	if type(product_price) == float or type(product_price) == int:
		if product_price > 0:
			receipt[product_name] = product_price

	return receipt



def edit_receipt(total,balance,payment,receipt):
	receipt["Total Paid"] = payment
	receipt["Grand Total"] = total
	receipt["Balance"] = balance
	return receipt
	
			
	
