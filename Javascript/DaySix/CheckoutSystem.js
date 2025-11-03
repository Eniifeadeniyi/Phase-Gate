let  prompt = require('prompt-sync')();

let invoice = {}
let receipt = {}

function makeInvoice(product,price){
	if(price > 0)invoice[product] = price
	return invoice;
}

function makeReceipt(product,price){
	if(price > 0) receipt[product] = price
	return receipt;
}

function getSubTotal(sum, price) {
	if(price > 0) sum += price
	return sum;
}

function getVAT(sum) {
	let vat = sum * 0.075;
	return vat;
}

function getTotal(sum,vat){
	let total = sum + vat;
	return total;
}

function editInvoice(sum, vat, total, invoice){
	invoice["Subtotal"] = sum
	invoice["VAT"] = vat
	invoice["Total Amount"] = total
	return invoice;
}

function checkPayment(payment,total) {
	if(payment > total) return "Overpay!";
	if(payment < 0) return "Invalid input!";
	if(payment >= 0) return payment;
}

function getBalance(total,payment) {
	let balance = total - payment
	return balance;
}


function editReceipt(total,balance,payment,receipt){
	receipt["Total Paid"] = payment
	receipt["Grand Total"] = total
	receipt["Balance"] = balance
	return receipt;
}

let product = prompt("Enter product name or type 'done' to finish: ");
let sum = 0;
while(product != "done") {
	let price = prompt("Enter price for " + product + " : ");
	sum = getSubTotal(sum,Number(price));	
	invoice = makeInvoice(product,Number(price));
	receipt = makeReceipt(product,Number(price));
	product = prompt("Enter product name or type 'done' to finish: ");
}
if(sum != 0) {
let tax = getVAT(sum)
let total = getTotal(sum,tax)
console.log("-----INVOICE-----")
console.log(editInvoice(sum,tax,total,invoice))
let payment = prompt("Enter payment amount: ")
let check = checkPayment(Number(payment),total)
while(check != Number(payment)) {
	console.log(check)
	payment = prompt("Enter payment amount: ")
	check = checkPayment(Number(payment))
}
let balance = getBalance(total,check)
receipt = editReceipt(total,balance,check,receipt);
console.log("-----RECEIPT-----")
console.log(receipt)
console.log("Payment successful! Thank you for shopping.")
}
else console.log("No purchases made!")
