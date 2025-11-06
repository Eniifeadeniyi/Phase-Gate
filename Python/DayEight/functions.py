def average(total,frequency):
	answer = total /frequency
	return (float(f"{answer:.2f}"))

def validate(score):
	if score.find(".") != -1:
		if score.strip().replace(".","",1).isdigit():
			if float(score) <= 100:
				return True
			else:
				return False
		else:
			return False
	if score.find(".") == -1:
		if score.strip().isdigit():
			if float(score) <= 100:
				return True
			else:
				return False
		else:
			return False
def minimum(numbers = []):
	smallest = numbers[0]
	for number in numbers:
		if number < smallest:
			smallest = number
	return smallest

def maximum(numbers = []):
	largest = numbers[0]
	for number in numbers:
		if number > largest:
			largest = number
	return largest

def descending(numbers : list):
	sorting = []
	while len(numbers) != 0:
		sorting.append(maximum(numbers))
		numbers.remove(maximum(numbers))	
	return sorting

def edit_numbers(original,new):	
	for count in range(len(original)):
		original[count] = new.index(original[count])+1
	return original


def trial(original,new):
	for count in range(len(original)):
		print(new.index(original[count])+1)







