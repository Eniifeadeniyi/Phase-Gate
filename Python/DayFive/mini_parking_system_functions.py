
def park(spaces,position):
	position = str(position)
	if position.isdigit():
		position = int(position)
		if position in spaces:
			spaces.remove(position)
			print("Car successfully parked!")
		else:
			return "Unavailable!"
	else:
		return "Invalid input!"	
	return spaces

def change_cars(spaces,cars,position):
	index = spaces.index(int(position))
	cars[index] = 1
	return cars	


def update_occupied(occupied, position):
	occupied.append(int(position))
	return occupied


def update_spaces(spaces,position):
	spaces.insert(int(position)-1,int(position))
	return spaces

def unpark(occupied,position):
	position = str(position)
	if position.isdigit():
		position = int(position)
		if position in occupied:
			occupied.remove(position)	
			print("Car successfully unparked!")
		else:
			return "Car not found!"
	else:
		return "Invalid input!"
	return occupied

def reverse_cars(cars,position):
	cars[int(position)-1] = 0
	return cars



