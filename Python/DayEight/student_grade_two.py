from functions_two import *

scores = []
total = []


number_of_students = input("Enter number of students: ")
number_of_subjects = input("Enter number of subjects: ")
while not number_of_students.strip().isdigit():
	print("Invalid input!")
	number_of_students = input("Enter number of students: ")

while not number_of_subjects.strip().isdigit():
	print("Invalid input!")
	number_of_subjects = input("Enter number of subjects: ")

if int(number_of_students) > 0 and int(number_of_subjects) > 0:
	while len(names) != int(number_of_students):
		name = input("Enter student's name: ")
		names = collect_names(name)
		make_record_keys()
	while len(subjects) != int(number_of_subjects):
		subject = input("Enter subject name: ")
		subs = collect_subject_names(subject)

	for sub in subs:	
		print("Enter scores for " + sub)	
		for name in names:
			subject_score = input("Enter score for " + name + ": ")			
			while not validate(subject_score):
				print("Invalid input!")
				subject_score = input("Enter score for " + name + ": ")

			record = make_record_value_keys(name,sub,float(subject_score))

	print("STUDENT     ", end = " ")
	for sub in subs:
		print(f"{sub}", end = "    ")
	print("TOT", end = "    ")
	print("AVE", end = "   ")
	print("POS")

	for key,value in record.items():
		summation = sum(value.values())
		total.append(summation)
	total1 = total.copy()
	new = descending(total)
	edit_numbers(total1,new)
	
	

	for key,value in record.items():
		print(f"{key}", end = " ")
		scores.clear()
		for subject,score in value.items():
			scores.append(score)
			total = sum(scores)
			mean = average(total,int(number_of_subjects))
			print(f"{score:>7.2f}", end = " ")
		print(f"{total:>7.2f}", end  = " ")
		print(f"{mean:>7}", end  = " ")
		#print(f"{total1:>7}")
		print()

	
		
		
	