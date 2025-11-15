#1
def make_new_word(word,ch):
	if not isinstance(word,str):
		return "Invalid input!"
	if word.isdigit():
		return "Invalid input!"
	if not isinstance(ch,str):
		return "Invalid input!"
	if ch.isdigit():
		return "Invalid input!"		
	for count in range(len(word)):
		if word[count] == ch:
			position = word.index(ch)
	if ch not in word:
		return word
	new_word = word[position::-1] + word[position+1:]
	return new_word

print(make_new_word("abcdefg", "g"))

#2
def unique(numbers = []):
	
	return count() < 2
numbers = [1,2,3,2]
print(list(filter(unique,numbers)))

#3
def sum_unique_elements(numbers = []):
	unique = []
	for number in numbers:	
		count = numbers.count(number)
		for count in range(1,2):
			if number not in unique:
				unique.append(number)	
			
	return unique

numbers = [1,2,2,3,4,4,5,6,6,7]
print(sum_unique_elements(numbers))


#4
def largest_lists(lists):
	position = []
	maximum = max(lists)
	position.append(lists.index(maximum))
	maxmus = max(maximum)
	position.append((maximum.index(maxmus)))
	return position
		
numbers = [[1.5,2.3,3.7,4.6],[5.1,6.2,7.3,8.4],[9.5,10.1,11.8,12.7]]

print(largest_lists(numbers))


#5
def count_element(word,character):
	count = 0
	for letter in word:
		if letter.lower() == character.lower():
			count += 1
	return count
print(count_element("OpenAI","a"))


#7
def maximum(numbers = []):
	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest

#8
def minimum(numbers = []):
	smallest = numbers[0]
	for number in numbers:
		if number < smallest:
			smallest = number
	return smallest
#6
def ascending(numbers = []):
	sorting = []
	while len(numbers) != 0:
		sorting.append(minimum(numbers))
		numbers.remove(minimum(numbers))	
	return sorting
numbers = [9,4,7,3]
print(ascending(numbers))


#9
def descending(numbers : list):
	sorting = []
	while len(numbers) != 0:
		sorting.append(maximum(numbers))
		numbers.remove(maximum(numbers))	
	return sorting
numbers = [9,4,7,3]
print(descending(numbers))

 

