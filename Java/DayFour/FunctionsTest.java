
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
		boolean[] answer = functions.Palindrome(new String[] {"madam", "racecar", "length"});
		boolean[] actual = System.out.print(Arrays.toString(answer));
		assertEquals(actual, [true, true, false]);
	}


}