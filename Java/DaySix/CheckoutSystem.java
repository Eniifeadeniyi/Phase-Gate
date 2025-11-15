import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class CheckoutSystem {
public static void main(String[] args) {
Scanner input = new Scanner(System.in);

ArrayList<String[]> invoice = new ArrayList<String[]>();
ArrayList<String[]> receipt = new ArrayList<String[]>();

double sum = 0.0;


System.out.print("Enter product name or type 'done' to finish: ");
String choice = input.nextLine();

while(!choice.equalsIgnoreCase("done")) {

System.out.print("Enter price for " + choice + ": ");
if(input.hasNextDouble() && !choice.trim().isEmpty()) {
	double price = input.nextDouble();
	if(price > 0) {
	String value = String.valueOf(price);
	sum += price;
	invoice.add(CheckoutSystemFunctions.makeInvoice(choice,value));
	receipt.add(CheckoutSystemFunctions.makeReceipt(choice,value));
	System.out.println("Purchase successful!");}
	else 
		System.out.println("Invalid input!");}
else
	System.out.println("Invalid input!");

input.nextLine();
System.out.print("Enter product name or type 'done' to finish: ");
choice = input.nextLine();
}

Double vat = 0.075 * sum;
Double total = sum + vat;
if(sum != 0.0) {
System.out.println("-----INVOICE-----");
for(String[] array : invoice) {
	System.out.printf("%s : %s %n",array[0],array[1]);}
System.out.printf("%s : %.2f \n","Subtotal",sum);
System.out.printf("%s : %.2f \n","VAT(7.5%)",vat);
System.out.printf("%s : %.2f \n","Total Amount",total);}

while(sum != 0.0) {
System.out.print("Enter payment amount: ");
if(input.hasNextDouble()) {
	double payment = input.nextDouble();
	if(payment >= total) {	
		double balance = payment - total;
		System.out.println("-----RECEIPT-----");
		for(String[] array : receipt) {	
			System.out.printf("%s : %s %n", array[0], array[1]);}
		System.out.printf("%s : %.2f %n", "Total Paid",payment);
		System.out.printf("%s : %.2f %n", "Grand Total", total);
		System.out.printf("%s : %.2f %n", "Balance", balance);
		System.out.print("Payment successful! Thank you for shopping!");
		break;
	  }
	if(payment < total && payment > -1) 
		System.out.println("Insufficient!");
	if(payment < 0) 
		System.out.println("Invalid input!");
}
else {
	System.out.println("Invalid input!");
	input.nextLine();
}		
	
}
if(sum == 0.0) System.out.print("No purchases made!");
}
}
