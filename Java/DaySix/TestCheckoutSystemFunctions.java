import java.util.Arrays;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestCheckoutSystemFunctions {
	

	@Test
	public void testThatMakeInvoiceWorks(){
		String[] actual =  CheckoutSystemFunctions.makeInvoice("Water", "500.50");
		String outcome = actual[0];
		String outcome1 = actual[1];
		assertEquals(outcome,"Water");
		assertEquals(outcome1,"500.50");
	}

	@Test
	public void testThatMakeReceiptWorks(){
		String[] actual =  CheckoutSystemFunctions.makeReceipt("Water", "500.50");
		String outcome = actual[0];
		String outcome1 = actual[1];
		assertEquals(outcome,"Water");
		assertEquals(outcome1,"500.50");
	}

}