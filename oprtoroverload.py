class poly():
	def __init__(self,a,b):
		self.a = a
		self.b = b



	def __add__(self,other):

		a = self.a+other.a
		b = self.b + other.b

		return	poly(a,b)
	def __repr__(self):
		return 'The sum is {}x+{}'.format(self.a,self.b)


exp1 = poly(4,5)
exp2 = poly(3,9)
print(exp1+exp2)