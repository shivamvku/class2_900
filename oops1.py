# class 
# =================


# syntax
# ---------------

# class classname(objets):
# 	body of the classs



# class a():
# 	print('hello i am the first class') --------- > readly avilabe

# print('This is my oops 1 fiel')


''' This is my file doc'''
# class Animal():
# 	'''This is my class doc'''
# 	anim1 = 'Loin'			#global var in the class
# 	anim2 = 'Tiger'

# print(Animal)
# print(Animal.anim1)
# print(Animal.anim2)
# print(__name__)

# Methods
# =====================
# Simple function written for class


# class Avngers():
# 	def details(fname,lname):
# 		print('The first name is :',fname)
# 		print('The Last name is :',lname)
# 	def pay(fname,amt):
# 		print('{} get paid {}'.format(fname,amt))
# 	def email(fname,lname):
# 		print('The email ID of the {0} is {0}.{1}@Avngers.com'.format(fname,lname))
# Avngers.details('Batman','Avngers')
# Avngers.pay('supermman',56000)
# Avngers.email('iromna','Reddy')


# class costructor
# predif sepcial method or magic method 
	# __init__ --------> initisation of clas var




class Avngers():
		# def __init__(fname,lname,amt):
		# 	fname = fname
		# 	lname = lname
		# 	amt = amt

	def details(fname,lname):
		print('The first name is :',fname)
		print('The Last name is :',lname)
		return 'somthng'
	def pay(fname,amt):
		print('{} get paid {}'.format(fname,amt))
	def email(fname,lname):
		print('The email ID of the {0} is {0}.{1}@Avngers.com'.format(fname,lname))
# Avngers.details('Batman','Avngers')
# Avngers.pay('supermman',56000)
# Avngers.email('iromna','Reddy')

# Avngers.details('Batman','Avngers')
# Avngers.pay('supermman',56000)
# Avngers.email('iromna','Reddy')


# objet
# ---------------------

avg1 = Avngers()
# print(avg1)

print(avg1.details('Batman','Avngers'))