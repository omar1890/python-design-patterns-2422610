#Factory pattern is a creational pattern for defining (instancting) a new type of specific object
class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Woof!"

	
	def get_pet(pet='dog'):

		"""The factory method"""
		pets = dict(dog=Dog("Hope"))
		return pets[pet]

class Cat:
    
	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def speak(self):
		return "Meow!"

def get_pet(pet='cat'):
    
		"""The factory method"""
		pets = dict(dog=Dog("Hope"),cat=Cat('Peace'))
		return pets[pet]

d = get_pet('dog')
print(d.speak())
c = get_pet('cat')
print(c.speak())