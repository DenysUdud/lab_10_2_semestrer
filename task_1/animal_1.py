# file: animal_1.py
# the file contains classes for representing animals.

class River_Object:
	"""
	A class used to represent animal.

	...

	Attributes
	----------
	name: str
	    The name of animal.
	position: int
	    The position of animal in list.

	Methods
	-------
	__eq__(other)
	    Method which compare two objects. If other is instance of
	    the object returns true.
	__del__()
	    Delete the object.
	set_position()
	   Method for changing position.
	"""

	def __init__(self, position, name):
		"""
		A method for initialisation of 
		:param name: str
		:param position: int
		"""
		self.name = name
		self.position = position

	def set_position(self, new_pos):
		"""
		A method for setting new position of object.
		:return: None
		"""
		self.position = new_pos

	def __del__(self):
		"""
		Deletes the object.
		:return: None
		"""

	def __eq__(self, other):
		"""
		A method used to compare two objects.
		:param other: object
		:return: bool
		"""
		if isinstance(other, self.__class__):
			return True
		else:
			return False

	def __repr__(self):
		"""
		A method for representing object in str form.
		:return: None
		"""
		return "<{}>".format(self.__class__.__name__)


class Bear(River_Object):
	"""
	A class represents bear in river eco-system.

	...

	Attributes
	----------
	name: str
	    The name of animal.
	position: int
	    The position of animal in list.

	Methods
	-------
	__eq__(other)
	    Method which compare two objects. If other is instance of
	    the object returns true.
	__del__()
	    Delete the object.
	set_position()
	   Method for changing position.
	"""
	def __init__(self, position, name="Bear"):
		"""
		A method for initialisation object.
		:param name: str
		:param position: int
		"""
		super().__init__(name, position)


class Fish(River_Object):
	"""
	A class represents fish in river eco-system.

	...

	Attributes
	----------
	name: str
	    The name of animal.
	position: int
	    The position of animal in list.

	Methods
	-------
	__eq__(other)
	    Method which compare two objects. If other is instance of
	    the object returns true.
	__del__()
	    Delete the object.
	set_position()
	   Method for changing position.
	"""
	def __init__(self, position, name="Fish"):
		"""
		A method for initialisation object.
		:param name: str
		:param position: int
		"""
		super().__init__(name, position)


class Water(River_Object):
	"""
	A class represents water in river.

	...

	Attributes
	----------
	name: str
	    The name of animal.
	position: int
	    The position of animal in list.

	Methods
	-------
	__eq__(other)
	    Method which compare two objects. If other is instance of
	    the object returns true.
	__del__()
	    Delete the object.
	set_position()
	   Method for changing position.
	"""
	def __init__(self, position, name="Water"):
		"""
		A method for initialisation water object.
		:param name:
		:param position:
		"""
		super().__init__(name, position)
