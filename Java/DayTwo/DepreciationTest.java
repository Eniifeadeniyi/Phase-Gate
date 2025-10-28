import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class DepreciationTest {

	@Test
	public void TestThatGetNumberOfItemsWorks() {
		Depreciation depreciation = new Depreciation();
		Double result = depreciation.getNumberOfYears(3);
		assertEquals(result,12.5);
	}
				


}

	