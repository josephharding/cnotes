import random

from animal import Animal

class Cat(Animal):
	
	def __init__(self):
		self.num_legs = 3


if __name__ == "__main__":
	maggie = Animal(3)
	pacer = Animal(8)
	my_string = "pacer legs: {p_legs}, maggie legs: {m_legs}"
	print(my_string.format(p_legs=pacer.get_num_legs(), m_legs=maggie.get_num_legs()))

	rand = random.Random()
	animallist=[]
	donecount=10
	while donecount > 0:
		animallist.append(Animal(rand.randint(2,8)))
		donecount = donecount - 1

	for animal in animallist:
		animal.feed()
	
	

