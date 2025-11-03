from checkout_system_functions import *
invoice = {}
receipt = {}
print("Welcome to Eni's Checkout System!")
product = input("Enter product name or type 'done' to finish: ")
while product.lower() != "done":
	price = input("Enter price for " + product + " : ")
	if price.isdigit() or price[-3] == ".":
		price = float(price)
		invoice = make_invoice(product,float(price))
		receipt = make_receipt(product,price)
	product = input("Enter product name or type 'done' to finish: ")

subtotal = get_sum(invoice)
if subtotal != 0:
	subtotal = get_sum(invoice)
	vat = get_vat(subtotal)
	total = get_total(subtotal,vat)
	invoice = edit_invoice(subtotal,vat,total,invoice)
	print("-----INVOICE-----")
	for key,value in invoice.items():
		print(f"{key} : {value}")
	payment = input("Enter payment amount: ")
	if not payment.isdigit():
		check = check_payment(payment,total)
		print(check)
	
	if payment.isdigit() or payment[-3] == ".":
		payment = float(payment)
		check = check_payment(payment,total)
		while check != payment:
			print(check)
			payment = input("Enter payment amount: ")
			check = check_payment(payment,total)
			if payment.isdigit() or payment[-3] == ".":
				payment = float(payment)
				check = check_payment(payment,total)
			
	
		balance = get_balance(total,payment)
		receipt = edit_receipt(total,balance,payment,receipt)
		print("-----Receipt-----")
		for key,value in receipt.items():
			print(f"{key} : {value}")
		print("Payment successful! Thank you for shopping.")

else:
	print("No purchases made!")

