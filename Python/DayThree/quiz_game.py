from quiz_game_functions import *

user_name = input("Enter your name: ")
print("Hi," + user_name + ", Welcome to Eni's quiz!")
count = 0

if user_name == "Chibuzor":
	count = 10
	numbers = [0,1,2,3,4,5,6,7,8,9]
	valid_options = ["a","b","c","d","A","B","C","D"]
	while(len(numbers) != 5):
		print(numbers)
		user_choice = input("Pick a number from above: ")
		if user_choice.isdigit() and int(user_choice) in numbers:
			print(get_question(int(user_choice)))
			print(get_option(int(user_choice)))
			user_answer = input("Enter answer: ")
			if user_answer.isdigit() or user_answer not in valid_options:
				print("Enter an option from above next time!")
			else:
				print(compare_answer(count, int(user_choice),user_answer))
				count = increase_score(count,int(user_choice),user_answer)
				numbers.remove(int(user_choice))
		else:
			print("Invalid input!")

else: 
	numbers = [0,1,2,3,4,5,6,7,8,9]
	valid_options = ["a","b","c","d","A","B","C","D"]
	while(len(numbers) != 0):
		print(numbers)
		user_choice = input("Pick a number from above: ")
		if user_choice.isdigit() and int(user_choice) in numbers:
			print(get_question(int(user_choice)))
			print(get_option(int(user_choice)))
			user_answer = input("Enter answer: ")
			if user_answer.isdigit() or user_answer not in valid_options:
				print("Enter an option from above next time!")
			else:
				print(compare_answer(count, int(user_choice),user_answer))
				count = increase_score(count,int(user_choice),user_answer)
				numbers.remove(int(user_choice))
		else:
			print("Invalid input!")


print(user_name + " , Your total is " + str(final_score(count)) + " over 10")


