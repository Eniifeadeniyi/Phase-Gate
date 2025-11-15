record = {}
names = []
proper_names =  []
subjects = []
proper_subjects = []

def collect_names(name):
	if not name.strip().isdigit() and name.strip() != "":
		if name.lower() not in names:
			names.append(name.lower())
			proper_names.append(name)
			print(name + " successfully added!")
		else:	
			print("Please, enter the initial of his/her surname!")
	else:
		print("Name should not contain numbers and shouldn't be empty!")
	return proper_names

def make_record_keys():
	for element in proper_names:
		record[element] = {}
	return record

def collect_subject_names(subject):
	if subject.strip() != "":
		if subject.lower() not in subjects:
			subjects.append(subject.lower())
			proper_subjects.append(subject)
			print(subject + " successfully added!")
		else:
			print("Subject already added!")
	else:
		print("Please enter a subject!")
	return proper_subjects


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

def make_record_value_keys(student, subject, score):
    record[student][subject] = score
    return record

def average(total,frequency):
	answer = total /frequency
	return (float(f"{answer:.2f}"))

def minimum(numbers : list):
	smallest = numbers[0]
	for number in numbers:
		if number < smallest:
			smallest = number
	return smallest

def maximum(numbers : list):
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
