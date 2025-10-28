public class Depreciation {

public Double getNumberOfYears(int numberOfItems) {
	Double total = numberOfItems * 50000.0;
	Double deduction = total * 0.08;
	Double times = total / deduction;
	return times;

}

}