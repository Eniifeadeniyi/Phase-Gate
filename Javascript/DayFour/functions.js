//1
function get_perfect_square(numbers) {
	for(let number in numbers) {
		let answer = numbers[number] ** 0.5
		if(numbers[number] % 2 == 0 & answer % 2 == 0) {
			numbers[number] = true;}
		if(numbers[number] % 2 != 0 & answer % 2 != 0) {
			numbers[number] = true;}
		if(numbers[number] % 2 == 0 & answer % 2 != 0) {
			numbers[number] = false;}
		if(numbers[number] % 2 != 0 & answer % 2 == 0) {
			numbers[number] = false;}
	}
	return numbers;
}
let numbers = [4,9,25,49,2,0,-2]
console.log(get_perfect_square(numbers))

//2
function get_palindrome_flags(strings) {
	for(let word in strings) {
		let reverse = ""
		let item = strings[word]
		for(let count = 0; count < item.length; count++) {
			reverse = item[count] + reverse;
		}
		if(reverse.toLowerCase() == item.toLowerCase()) {
			strings[word] = true;}
		else{
			strings[word] = false;}
	}
	return strings;
}
let strings = ["Madam", "racecar", "hello", "12321", "me", "44"]
console.log(get_palindrome_flags(strings))



