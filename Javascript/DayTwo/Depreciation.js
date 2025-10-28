function getNumberOfYearsTillFreeGood(number_of_items) {
	let total = number_of_items * 50000;
	let deduction = total * 0.08;
	let times = total / deduction;
	return times;
}


console.log(getNumberOfYearsTillFreeGood(3));