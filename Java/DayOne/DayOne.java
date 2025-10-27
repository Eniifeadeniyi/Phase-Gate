import java.util.Scanner;
public class DayOne {
public static void main(String[] args) {
Scanner input = new Scanner(System.in);

int countCorrect = 0;
for(int count = 0; count < 10; count++) {
	Double firstNumber = Math.floor(Math.random()  * 100);
	Double secondNumber = Math.floor(Math.random() * 100);
	Double answer = firstNumber - secondNumber;
	
	System.out.print("What is " + firstNumber + " minus " + secondNumber + ": ");
	int userInput = input.nextInt();
	
	if(userInput == answer) {
		countCorrect += 1;
	}
	
	if(userInput != answer) {
		System.out.print("Try again: ");
		int userInputTwo = input.nextInt();
		if(userInputTwo != answer) {
			System.out.println("The correct answer is : " + answer);
		}
	}
	
}
System.out.print("You answered " + countCorrect + " questions out of 10 questions correctly!");

}
}