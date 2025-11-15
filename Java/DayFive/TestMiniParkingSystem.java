import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import java.util.ArrayList;

public class TestMiniParkingSystem {
	
	
	@Test
	public void testThatParkWorks() {
		ArrayList<Integer> spaces = new ArrayList<Integer>();
		for(int i = 1; i < 11; i++){
		spaces.add(i);}
		ArrayList<Integer> actual = MiniParkingSystemFunctions.Park(spaces,5);
		assertEquals(actual,spaces);
	}

}