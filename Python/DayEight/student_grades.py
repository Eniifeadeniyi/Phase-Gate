from functions import *
student = {}
totals = []
positions = []
maxes = []
passes = 0
fails = 0
tots = []
maxbiggest = []
leastsmallest = []
totals1 = []

students = input("Enter number of students: ")
while not students.strip().isdigit():
	print("Invalid input!")
	students = input("Enter number of students: ")

subjects = input("Enter number of subjects: ")
while not subjects.strip().isdigit():
	print("Invalid input!")
	subjects = input("Enter number of subjects: ")
	
if int(students) > 0 and int(subjects) > 0:
	for count in range(1,int(students)+1):
		student[count] = {}
		for counter in range(1,int(subjects)+1):
			score = input("Enter score for student " + str(count) + " for subject " + str(counter) + ": ")
			while not validate(score):		
				print("Invalid input")
				score = input("Enter score for student " + str(count) + " for subject " + str(counter) + ": ")
			student[count][counter] = float(score)
	

	print("STUDENT     ", end = " ")
	for sub in range(1,int(subjects)+1):
		print(f"SUB{sub}",end = "    ")
	print("TOT", end = "    ")
	print("AVE", end = "   ")
	print("POS")



	for key,value in student.items():
		print(f"Student {key}", end = " ")
		total = sum(value.values())
		totals.append(total)
		totals1.append(total)
		new = sorted(totals, reverse = True)
		mean = average(total,int(subjects))
		for grade in value.values():
			print(f"{grade:>7}", end = " ")
		print(f"{total:>6}", end = " ")
		print(f"{mean:>6}", end = " ")		
		print()
	print(edit_numbers(totals,new))
	
	print()

	print("SUBJECT SUMMARY")
	for count in range(1,int(subjects) + 1):
		maxes.clear()
		for key,value in student.items():
			score = value[count]
			maxes.append(score)
			
		biggest = maximum(maxes)
		maxbiggest.append(biggest)
		total = sum(maxes)
		ave = average(total,key)
		least = minimum(maxes)
		leastsmallest.append(least)
		person = maxes.index(biggest) + 1
		person1 = maxes.index(least) + 1
		tots.append(ave)
		for element in maxes:
			if element >= 50:
				passes += 1
			else:
				fails += 1
		
		
		print(f"Subject {count}")
		print(f"Highest scoring student is: Student {person} scoring {biggest}")
		print(f"Lowest scoring student is: Student {person1} scoring {least}")
		print(f"Total Score is: {total}")
		print(f"Average score is: {ave}")
		print(f"Number of Passes: {passes}")
		print(f"Number of Fails: {fails}")
		print()

	hardsub = tots.index(minimum(tots)) + 1
	easysub = tots.index(maximum(tots)) + 1
	print(f"The hardest subject is Subject {hardsub} with failures ")
	print(f"The easiest subject is Subject {easysub} with failures ")
	print(f"The overall Highest score is scored by Student {person} in Subject {maxbiggest.index(maximum(maxbiggest))+1} scoring {maximum(maxbiggest)}")
	print(f"The overall Lowest score is scored by Student {person1} in Subject {leastsmallest.index(minimum(leastsmallest))+1} scoring {minimum(leastsmallest)}")
	
	print()	

	print("CLASS SUMMARY")
	winner = maximum(totals1)
	loser = minimum(totals1)
	print(f"Best Graduating Student is: Student {totals1.index(winner)+1} scoring {winner}")
	print(f"Worst Graduating Student is: Student {totals1.index(loser)+1} scoring {loser}")
	print(f"Class total score is: {sum(totals1)}")
	print(f"Class Average score is: {average(sum(totals1),len(totals1))}")
			
	
	
	

else:
	print("No records!")

	

