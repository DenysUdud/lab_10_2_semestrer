# file: river_1.py
# This module represents eco-system.
from task_1.animal_1 import *
import random

class NoPlaceError(BaseException):
	"""
	Error which occurs when there is not empty space in the
	eco-system.
	"""
	pass


class River:
	"""
	A class used to represent and generate river.

	...

	Attributes
	----------
	size: int
	    The len of list which represents river.
	bear_quant: int
	    The number of bears in river eco-system.
	fish_quant: int
	    The amount of fish in river eco-system.
	water_quant: int
	    The amount of water in river eco-system.
	river_lst: list
	    The list which represents river and chars there.

	Methods
	-------
	__repr__()
	    Method represents river in str form.
	add_animal()
	    Method adds animals to certain pos in list.
	get_quantity(object)
	    Returns the number of certain class's objects in the river.
	generate_river()
	    Generates river of certain size.
	get_inf()
	    Returns information about all inhabitants in the river.
	"""

	def __init__(self, size):
		"""
		Method for initialising eco-system.
		:param size: int
		"""
		self.size = size
		self.bear_quant = 0
		self.fish_quant = 0
		self.water_quant = 0
		self.river_lst = []

	def __repr__(self):
		"""
		A method represents river in str form.
		:return: str
		"""
		string = ""
		for obj in self.river_lst:
			if isinstance(obj, Bear):
				string += "|🐻|"
				self.bear_quant += 1
			elif isinstance(obj, Fish):
				string += "|🐠|"
				self.fish_quant += 1
			else:
				string += "|🌊|"
				self.water_quant += 1
		return string

	def generate_river(self):
		"""
		Generates river of certain size.
		:return: None
		"""
		river = self.river_lst
		for i in range(self.size):
			random_num = random.randint(0, 2)
			if random_num == 0:
				river.append(Water(i))
			elif random_num == 1:
				river.append(Bear(i))
			else:
				river.append(Fish(i))

	def add_animal(self, animal_object):
		"""
		A method adds animal in the certain position of list.
		:param position: int
		:param animal_object: object
		:return: None
		"""
		rand_lst = []
		for i in range(self.size):
			if isinstance(self.river_lst[i], Water):
				rand_lst.append(i)
		if len(rand_lst) <= 0:
			raise NoPlaceError
		position = random.choice(rand_lst)
		if isinstance(animal_object, Bear):
			self.river_lst[position] = Bear(position)
		elif isinstance(animal_object, Fish):
			self.river_lst[position] = Fish(position)
		else:
			self.river_lst[position] = Water(position)

	def get_quantity(self, animal_object):
		"""
		A method returns quantity of animals of certain class in
		river lst.
		:param animal_object: the object class
		:return: int
		"""
		if isinstance(animal_object, Bear):
			return self.bear_quant
		elif isinstance(animal_object, Fish):
			return self.fish_quant
		else:
			return self.water_quant

	def get_inf(self):
		"""
		Returns inf about inhabitants of river.
		:return: str
		"""
		return "There are {} Bears; {} Fishes; {} Water".format(
			self.bear_quant, self.fish_quant, self.water_quant
		)
