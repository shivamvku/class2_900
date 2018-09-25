

# Method OverRigdig
# ======================


class A():
	def m1(self):
		print('I am from class A Method -1')
	def m21(self):
		print('I am from class A Method -2')
class B(A):
	def mb1(self):
		print('I am from class B Method -1')
	def m2(self):
		super().m2()
class d(A):
	def m2(self):
		print('sdasd')


o1 = B()
o1.m2()

# o2 = A()
# o2.m2()

a = d()
a.m21()

