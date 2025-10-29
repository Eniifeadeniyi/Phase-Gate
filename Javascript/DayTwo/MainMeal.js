function arrange(numbers) {
	let sorting = []
	let maximum = 0
	for (number in numbers) {
		if (number > maximum) maximum = number
		while(numbers.length != 0){
			sorting.push(maximum)
			let value = numbers.indexOf(maximum)
			numbers.splice(value,1)
		}
	}
	return sorting
}
numbers = [3,9,8,7]
console.log(arrange(numbers))



































/*
//new_word = word.slice(position,0,-1) + word.slice(position+1,-1,1)


function makeNewWord(word,ch) {
	for(let letter in word) {
		if(letter == ch) {
			return letter;
		}
	}
}


console.log(makeNewWord("abcdefd", "d"))



//5
function countElement(word,character) {
	//let count = 0;
	//let letters = word.split(',');
	let count = 0;
	for(;count < word.length;) {
		if(word.charAt(count) == character) {
			 count++;}
	}

	return count;
}

console.log(countElement("OpenAi", "n"))
*/