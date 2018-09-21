
class Avngers():
	def __init__(self,fname,lname,amt):
		self.fname = fname
		self.lname = lname
		self.amt = amt

		# print(self.fname)
		# print(self.lname)
		# print(self.amt)

	def details(self):
		print('The first name is :',self.fname)
		print('The Last name is :',self.lname)
	# 	return 'somthng'
	def pay(self):
		print('{} get paid {}'.format(self.fname,self.amt))

	def email(self):
		print('The email ID of the {0} is {0}.{1}@Avngers.com'.format(self.fname,self.lname))


# objet
# ---------------------

avg1 = Avngers('Batman','Avngers',5000)
avg2 = Avngers('supermna','rao',300)
avg3 = Avngers('Ironman','reddy',400)

avg1.details()
avg2.details()
avg3.details()


avg1.pay()
avg2.pay()
avg3.pay()

avg1.email()
avg2.email()
avg3.email()