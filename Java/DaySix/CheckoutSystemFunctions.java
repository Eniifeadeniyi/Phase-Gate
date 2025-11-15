public class CheckoutSystemFunctions {


	public static String[] makeInvoice(String product, String price) {
		String[] productsAndPrices = new String[2]; 
			productsAndPrices[0] = product;
			productsAndPrices[1] = price;
		return productsAndPrices;
}
	
	public static String[] makeReceipt(String product, String price) { 
		String[] productsAndPrices = new String[2];
			productsAndPrices[0] = product;
			productsAndPrices[1] = price;
		return productsAndPrices;
}


	
}		