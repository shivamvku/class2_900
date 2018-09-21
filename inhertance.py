# # INHERTANCE
# # --------------------

# # Multiple t-1
# # --------------------



# class Animal():
# 	def __init__(self,name):
# 		self.name = name

# 	def eat(self):
# 		print("The {} is eating ".format(self.name))
# 	def sleep(self):
# 		print('The {} is sleeping'.format(self.name))

# class Loin(Animal):
# 	def roar(self):
# 		print('{} is roaring'.format(self.name))
# 	def hunt(self):
# 		print('{} is Hunting'.format(self.name))

# class Amphibians(Animal):
# 	def swim(self):
# 		print('{} is swiming'.format(self.name))
# 	def pound(self):
# 		print('{} is pounding'.format(self.name))

# class Tiger(Animal):
# 	"""docstring for Tiger"""
# 	def climb(self):
# 		print('{} is climbing'.format(self.name))
# 	def Run(self):
# 		print('{} is running'.format(self.name))


# t1 = Tiger('Vijay')
# t1.climb()
# t1.Run()

# t1.sleep()
# t1.eat()

# t1.roar()
# t1.hunt()

# ====================================================================

# INHERTANCE
# --------------------

# Multiple t-2
# --------------------



# class Animal():
# 	def __init__(self,name):
# 		self.name = name

# 	def eat(self):
# 		print("The {} is eating ".format(self.name))
# 	def sleep(self):
# 		print('The {} is sleeping'.format(self.name))

# class Loin():
# 	def roar(self):
# 		print('{} is roaring'.format(self.name))
# 	def hunt(self):
# 		print('{} is Hunting'.format(self.name))

# class Amphibians(Animal):
# 	def swim(self):
# 		print('{} is swiming'.format(self.name))
# 	def pound(self):
# 		print('{} is pounding'.format(self.name))

# class Tiger(Loin,Amphibians):
# 	"""docstring for Tiger"""
# 	def climb(self):
# 		print('{} is climbing'.format(self.name))
# 	def Run(self):
# 		print('{} is running'.format(self.name))


# t1 = Tiger('Vijay')
# t1.eat()
# t1.sleep()
# t1.pound()

# # l1 = Loin('Sheru')
# f1 = Amphibians('nemo')
# t1.climb()
# t1.Run()

# t1.sleep()
# t1.eat()

# t1.roar()
# t1.hunt()

# # l1.eat()
# # l1.roar()

# f1.swim()
# f1.sleep()
# t1.swim()




class Animal():
	def __init__(self,name):
		self.name = name
	def eat(self):
		print("The {} is eating ".format(self.name))
	def sleep(self):
		print('The {} is sleeping'.format(self.name))

class Loin(Animal):
	def roar(self):
		print('{} is roaring'.format(self.name))
	def hunt(self):
		print('{} is Hunting'.format(self.name))

class Amphibians(Loin):
	def swim(self):
		print('{} is swiming'.format(self.name))
	def pound(self):
		print('{} is pounding'.format(self.name))

class Tiger(Amphibians):
	"""docstring for Tiger"""
	def climb(self):
		print('{} is climbing'.format(self.name))
	def Run(self):
		print('{} is running'.format(self.name))




# t1 = Tiger('Vijay')
# t1.climb()
# t1.Run()
# t1.swim()
# t1.hunt()
# t1.eat()

f1 = Amphibians('Nemo')
f1.eat()
f1.hunt()
f1.swim()

















