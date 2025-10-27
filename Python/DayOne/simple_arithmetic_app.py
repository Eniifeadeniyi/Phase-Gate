import random
import datetime
 
start = datetime.datetime.now()
count_correct = 0
count = 0
choice = "yes"
while choice != "no" and count < 10:
	first_number = random.randint(0,100)
	second_number = random.randint(0,100)

	minimum = min(first_number,second_number)
	maximum = max(first_number,second_number)
	answer = maximum - minimum

	
	user_input = float(input("What is " + str(maximum) + " - " + str(minimum) + "?: "))

	if user_input == answer:
		count_correct += 1

	if user_input != answer:
		user_input_2 = float(input("Try again: "))

		if user_input_2 != answer:
			print("The correct answer is: " + str(answer))
	count += 1
	if count < 10:
		choice = input("Would you like another question?: ").lower()


print("You answered " + str(count_correct) + " questions correctly out of " + str(count) + " questions!")
end = datetime.datetime.now()
print("Time taken: " + str(end - start))



