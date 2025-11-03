import java.util.ArrayList;
import java.util.Scanner;
public class CheckoutSystem {
public static void main(String[] args) {
Scanner input = new Scanner(System.in);

ArrayList<ArrayList> invoice = new ArrayList<ArrayList>();


System.out.print("Enter product name or type 'done' to finish: ");
String choice = input.nextLine();

while(!choice.equalsIgnoreCase("done")) {

System.out.print("Enter price for " + choice + " : ");
double price = input.nextDouble();

CheckoutSystemFunctions.makeInvoice(choice,price,invoice);

input.nextLine();
System.out.print("Enter product name or type 'done' to finish: ");
choice = input.nextLine();
}

System.out.print(invoice);
}
}
