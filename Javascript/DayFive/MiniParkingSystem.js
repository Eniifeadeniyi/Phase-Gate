let spaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
let occupied = []
let cars = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
function change(spaces,position) {
	let index = spaces[position]
	cars[index] = 1
	return cars;
}

function updateOccupied(position) {
	occupied.push(position)
	return occupied;
}

function updateSpaces(position) {
	spaces.splice(position-1,0,position)
	return spaces
}

function unpark(occupied,position) {
	cars[position] = 0;
	return cars;
}

function remove(list,item) {
	let temp = list.at(-1);
	let index = list.indexOf(Number(item))
	list[list.length-1] = list[index]
	list[index] = temp
	list.pop();
	return list
}

let prompt = require('prompt-sync')();

console.log("Welcome to Eni's parking lot!");

let choice = 0;
while(choice != 3) {
console.log("1. Park");
console.log("2. Unpark");
console.log("3. Exit");

choice = prompt("Enter operation: ");
switch(choice) {
	case "1" : 
	if(spaces.length != 0) {
		console.log(spaces)
		let position = prompt("Enter a number from above to park your car: ");
		if(occupied.includes(Number(position))) console.log("Occupied!");
		position = Number(position);
		if(spaces.includes(position)) {
		change(spaces,position);
		updateOccupied(position);
		remove(spaces,position);
		console.log("Car successfully parked!");
		}
		else console.log("Invalid input!");
		
	
	}
	break;

	case "2" :
	if(occupied.length != 0) {
		console.log(occupied);
		let index = prompt("Enter number you parked your car in: ");
		if(spaces.includes(Number(index))) console.log("No car found!");
		if(Number(index) >= 21 | Number(index) < 1) console.log("Invalid input!");
		index = Number(index);
		if(occupied.includes(index)) {
			unpark(occupied,index);
			updateSpaces(index);
			remove(occupied,index)
			console.log("Car successfully unparked!");
			}
		}
	else console.log("No cars parked yet!");
	break;
	
	case "3" :
		console.log("Goodbye!");
		break;
	
	default:
		console.log("Invalid operation!");

	
	
	
}
}
	
	