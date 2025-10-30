
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;

public class FunctionsTest {

	Functions function;
	@BeforeEach 
	void setup() {
		function = new Functions(); }

	@Test
	public void PalindromeWorks() {
		boolean[] actual = function.palindrome(new String[] {"madam"});
		boolean[] expected = {false};
		assertEquals(actual,expected);
	}


}