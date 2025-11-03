import java.util.ArrayList;
public class CheckoutSystemFunctions {


ArrayList<ArrayList> invoice = new ArrayList<ArrayList>();



	public static ArrayList makeInvoice(String product, double price, ArrayList invoice) { 
	ArrayList<String> products = new ArrayList<String>();
	ArrayList<Double> prices = new ArrayList<Double>();
			products.add(product);
			prices.add(price);
			invoice.add(products);
			invoice.add(prices);
		return invoice;
}
	
}		