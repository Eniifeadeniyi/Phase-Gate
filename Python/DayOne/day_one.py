import random
import datetime
 
start = datetime.datetime.now()
count_correct = 0
for _ in range(10):
	first_number = random.randint(0,100)
	second_number = random.randint(0,100)
	answer = first_number - second_number

	user_input = int(input("What is " + str(first_number) + " - " + str(second_number) + "?: "))
	if user_input == answer:
		count_correct += 1

	if user_input != answer:
		user_input_2 = int(input("Try again: "))

		if user_input_2 != answer:
			print("The correct answer is: " + str(answer))

print("You answered " + str(count_correct) + " questions correctly out of 10 questions!")
end = datetime.datetime.now()
print("Time taken: " + str(end - start))