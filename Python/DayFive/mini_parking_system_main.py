from mini_parking_system_functions import *

spaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cars = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
occupied = []


print("Welcome to Eni's Parking Lot!")
menu = """
	1. Park
	2. Unpark
	3.Exit
	"""
operation = ""
while(operation != "3"):
	print(menu)
	operation = input("Enter an operation: ")
	match operation:
		case "3" :
			print("Goodbye!")
		case "1" : 
			print(spaces)
			position = input("Enter a number from above to park: ")
			if position.isdigit() and int(position) not in spaces:
				print(park(spaces,int(position)))
			if position.isdigit() and int(position) in spaces:
				change_cars(spaces,cars,int(position))
				occupied = update_occupied(occupied,int(position))
				spaces = park(spaces,position)
			if not position.isdigit():
				print("Invalid input!")
		
		case "2" :
			if len(occupied) == 0:
				print("No cars parked yet!")
			else:
				print(occupied)
				position = input("Enter number you parked your car in: ")
				if position.isdigit() and int(position) not in occupied:
					print(unpark(occupied,int(position)))
				if position.isdigit() and int(position) in occupied:
					reverse_cars(cars,int(position))
					space = update_spaces(spaces,position)
					occupied = unpark(occupied,position)

				if not position.isdigit():
					print("Invalid input!")							

		
		case _: 
			print("Invalid input!")
			