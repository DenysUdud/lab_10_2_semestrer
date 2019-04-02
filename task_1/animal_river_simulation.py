# file: river_1.py
# This module represents eco-system.
from task_1.animal_1 import *
from task_1.river_1 import *
import random


def simulation_starter(size):
	"""
	The function which starts the simulation.
	:param size: size of river (lst): int
	:return: None
	"""
	river = River(size)
	river.generate_river()
	river_lst = river.river_lst
	print("There is your river\n")
	print(river)
	print(river.get_inf())
	try:
		counter = 1
		while True:
			print("\n{} cycle of modeling!".format(counter))
			# init_ind - initial index - index of animal which
			# will migrate.
			init_ind = random.randint(0, size - 1)
			# if random char is water we choose another one.
			while isinstance(river_lst[init_ind], Water):
				init_ind = random.randint(0, size - 1)
			# direct - left or right or nor migration
			direct = random.randint(-1, 1)
			# choose position to migrate to
			f_ind = final_ind(direct, init_ind, river_lst)
			# watching what animal is in initial posit and making act
			obj = river_lst[init_ind]
			# make migration
			animal_interaction(obj, init_ind, f_ind, river_lst,
							   river)
			print("There is river eco-system! ⬇️ ")
			print(river)
			counter += 1
	except NoPlaceError:
		print("River doesn't have place to migrate to or "
			  "there is not place for new bears!")
		return


def final_ind(direct, init_index, lst):
	"""
	The function which return final position in list after migration.
	:param direct: int
	:param lst: list
	:return: int

	>>>final_ind(-1, 2, [0,2,1])
	1
	"""
	if direct == -1 and init_index != 0:
		return init_index + direct
	elif direct == 1 and init_index != len(lst) - 1:
		return init_index + direct
	else:
		return 0


def animal_interaction(obj, init_ind, final_ind, river_lst, river):
	"""
	A function changes list.
	If bear go to position of fish - bear go to new position and fish
	deletes.
	If animals of the same class meets in one position - new object
	of this class creates.
	If animal go to the water position, water deletes and animal
	changes its position.
	:param obj: object - the object in initial position.
	:param init_ind: int - initial index of object
	:param final_ind: int - the final position of the object
	                        (destination)
	:param river_lst: list -  the list which represents river
	:param river - river object.
	"""
	if obj == river_lst[final_ind] and not isinstance(
			obj, Water) and \
			final_ind != 0:
		river.add_animal(obj)
		if isinstance(obj, Bear):
			print("Two bears came up!")
		elif isinstance(obj, Fish):
			print("Two fishes came up!")
	elif (isinstance(river_lst[final_ind], Fish) and
		  isinstance(river_lst[init_ind], Bear)) or \
		 (isinstance(river_lst[final_ind], Bear) and
		  isinstance(river_lst[init_ind], Fish)):
		print("Bear ate fish!")
		river_lst[final_ind] = Bear(final_ind)
		river_lst[init_ind] = Water(init_ind)
	elif obj == river_lst[final_ind] and not isinstance(obj,Water):
		print("Nobody wanted migrate somewhere!")
	# If there is errors this thing came out.
	elif isinstance(river_lst[final_ind], Water) and not isinstance(obj, Water):
		river_lst[final_ind] = river_lst[init_ind]
		river_lst[init_ind] = Water(init_ind)
		if isinstance(obj, Bear):
			print("Bear moved to another position!")
		elif isinstance(obj, Fish):
			print("Fish moved to another position!")
	else:
		# it will occur if there is smth wrong.
		print("Nothing happend!🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔")


if __name__ == "__main__":
	size = input("Type size of river eco-system: ")
	simulation_starter(int(size))
