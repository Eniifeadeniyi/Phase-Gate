def get_perfect_square(numbers):
	for count in range(len(numbers)):
		numbers[count] = str(numbers[count])
		if numbers[count].isdigit():
			numbers[count] = int(numbers[count])
			answer = numbers[count] ** 0.5
			if numbers[count] % 2 == 0 and answer % 2 == 0:
				numbers[count] = True
			elif numbers[count] % 2 != 0 and answer % 2 != 0:
				numbers[count] = True
		
			elif numbers[count] % 2 == 0 and answer % 2 != 0:
				numbers[count] = False
			
			elif numbers[count] % 2 != 0 and answer % 2 == 0:
				numbers[count] = False
		else:
			numbers[count] = "Invalid!"
			
	return numbers
print(get_perfect_square([2,4,7,-10,626,126]))

#2
def get_palindrome_flags(words):
	for count in range(len(words)):		
		word = str(words[count])
		reverse = ""

		if word.isdigit():
			if int(word) < 10:
				words[count] = True

		for letter in word:
			reverse = letter + reverse
		if reverse.lower() == word.lower():
			words[count] = True
		if reverse.lower() != word.lower():
			words[count] = False
		
	return words
print(get_palindrome_flags(["Madam", 45, 5, "length"]))

			