# super () ------- > working it refers to inmmediaet super class

# class Animal():
# 	def __init__(self,name1):
# 		self.name1 = name1
# 	def eat(self):
# 		print("The {} is eating ".format(self.name1))
# 	def sleep(self):
# 		print('The {} is sleeping'.format(self.name1))
# 	def ex1(self):
# 		print('helo this is first class')

# class Loin(Animal):
# 	def __init__(self,name2,name1):
# 		self.name2 = name2
# 		super().__init__(name1)
		
# 		super().ex1()

# 	def roar(self):
# 		print('{} is roaring'.format(self.name2))
# 	def hunt(self):
# 		print('{} is Hunting'.format(self.name2))




# l1 = Loin('leo','shreu')
# l1.roar()
# l1.eat()
# l1.ex1('hello')


# class Animal():
# 	def __init__(self,animname2):
# 		self.animname2 = animname2
# 	def eat(self):
# 		print('{} is eating'.format(self.animname2))
# 	def sleep(self):
# 		print('{} is sleeping'.format(self.animname2))

# class AquaAnimals():
# 	def __init__(self,animname3):
# 		self.animname3 = animname3
# 	def swim(self):
# 		print('{} is swiming'.format(self.animname3))
# 	def hunt(self):
# 		print('{} is hunting'.format(self.animname3))

# class wildAnimal(AquaAnimals,Animal):
# 	def __init__(self,animname1):
# 		self.animname1 = animname1
# 		super().__init__(animname2)		
# 		super(AquaAnimals,self).__init__(animname3)
# 	def climb(self):
# 		print('{} is climbing'.format(self.animname1))
# 	def bite(self):
# 		print('{} is biting'.format(self.animname1))

# w1 = wildAnimal('loin','Tiger','cheeta')

# # w1.climb()
# # w1.eat()

# w1.swim()
# w1.eat()