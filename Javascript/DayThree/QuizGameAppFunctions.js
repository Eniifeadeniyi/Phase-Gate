let answers = ["A", "C", "B", "C", "B", "C", "A", "B", "C", "D"]

let questions = ["Who was swallowed by a large fish?", "What is the first book of the New Testament?", "Who had a dream about a giant statue made of gold, silver, bronze, iron, and clay?", "Which disciple denied Jesus three times?", "What did God create on the first day?", "Who killed Goliath?", "Which disciple betrayed Jesus for thirty pieces of silver?", "Where is the shortest verse in the Bible found?", "Who led the Israelites out of Egypt?", "What kind of fruit did Adam and Eve eat in Eden?"]

let options = ["A. Jonah | B. Moses | C. Peter | D. Elijah", "A. Luke | B. Mark | C. Matthew | D. John", "A. Solomon | B. Nebuchadnezzar | C. Pharaoh | D. Ahab", "A. Andrew | B. John | C. Peter | D. James", "A. Animals | B. Light | C. Plants | D. Stars", "A. Saul | B. Samson | C. David | D. Jonathan", "A. Judas Iscariot | B. Thomas | C. Matthew | D. Philip", "A. Psalm 103:119 | B. John 11:35 | C. John 1:1 | D. Exodus 14:14", "A. Abraham | B. Joseph | C. Moses | D. Joshua", "A. Apple | B. Grapes | C. Banana | D. Bible didn’t say"]

indexes = [];

function get_random_index() {
	index = Math.floor(Math.random() * 10);
	return index;
}

function edit_indexes(index) {
	indexes.push(index);
	return indexes;
}

function confirm_different_index(index) {
	index = Math.floor(Math.random() * 10);
	for(let int of indexes) {
		if(index == int) index = Math.floor(Math.random() * 10);
	}
	return index
}

function get_question(index) {
	return questions[index];
}

function get_options(index) {
	return options[index];
}

function compare_answer(answer,index) {
	if(answer.toUpperCase() == answers[index])
		return "Correct!";
	else {
		return"Oops!!!";
	}
}

function increase_score(answer,index,score) {
	if(answer.toUpperCase() == answers[index]) score += 1
	return score;
}

function final_score(score) {
	return score;
}


let prompt = require('prompt-sync')();

let name = prompt('Enter your name: ');
console.log("Welcome, " + name);
console.log("There are 10 questions in total!")
console.log("Goodluck, and remember to have fun!")

let score = 0;
for(let count = 0; count < 10; count++) {
let index = get_random_index();
edit_indexes(index);
index = confirm_different_index(index);
console.log(get_question(index));
console.log(get_options(index));
let answer = prompt("Enter answer: ")
console.log(compare_answer(answer,index));
score = increase_score(answer,index,score);
}
console.log("You scored " + final_score(score) + " over 10")

//trying out another method(the way i did python)
/*
let numbers = [0,1,2,3,4,5,6,7,8,9];
while(numbers.length() != 0) {
console.log(numbers);
let choice = prompt("Enter a number from numbers above: ");
if(numbers.contains(choice)) {
let temp = numbers.at(-1);
numbers[numbers.length-1] = numbers[choice]
numbers[choice] = temp
numbers.pop()
}
else {
	console.log("Please, enter an available number!")

}
*/

