let prompt = require('prompt-sync')();

let count_correct = 0;
for(let count = 0; count < 10; count++) {
	let first_number = Math.floor(Math.random() * 100);
	let second_number = Math.floor(Math.random() * 100);
	let answer = first_number - second_number;
	

	let user_input = prompt("What is " + first_number + " minus " + second_number + " : ");

	if(user_input == answer) {
		countCorrect += 1;
	}
	
	if(user_input != answer) {
		let user_input2 = prompt("Try again: ");
		if(user_input2 != answer) {
			console.log("The correct answer is: " + answer);
		}
	}

}

console.log("You answered " + count_correct + " questions out of 10 questions correctly!");
