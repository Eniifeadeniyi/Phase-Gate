import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestCheckoutSystemFunctions {
	
	ArrayList<ArrayList> invoice = new ArrayList<ArrayList>();
	@Test
	public void testThatMakeInvoiceWorks(){
		ArrayList actual =  CheckoutSystemFunctions.makeInvoice("Water", 500.50,invoice);
		ArrayList expected = [[Water],[500.50]]
		assertEquals(actual, expected);
	}
}