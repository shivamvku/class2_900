# # Arbitary or varbale length argumets
# ______________________________________


# # type - 1
# _----------

# *args ----------  > convention


# def greeting(*name):
# 	for i in name:
# 		print('Hello', i,'welcom to digtal lync')

# greeting('Batman','Supermna','Ironmamn','Wonderwomn')


# hello Batman welcom to digtal lync


# type - 2
# -------------------

# a,b,c = [a for a in range(0,11)],[a for a in range(20,30)],[a for a in range(40,50)]

# print(a)
# print(b)

# .keys()
# .values()
# .items()

# print(c)


# # **kwargs ------------> convention
# def greeting(**val):
# 	print(val)
# 	# for i,j in val.items():
# 	# 	print('hello',i,'Welcome to ',j)
# greeting(Batman= {'usa','asdasd','asdasdasd'},Ironmamn = {'ua','dsd','asdasdasd'},Supermna = 'Pakistan')

# postion , default , *args, **kwargs



# Anonmys function or lambda function or arbitary function
 # -------------------------------------------------------


# synxt
# -------------
# by default there is  return type in lambda function

# fun defination
# -----------------------
# lambda arg:expressions

# var = lambda arg:expressions
 
# function call
# var(parameterts)


# squ = lambda:print('hello from lambda')
# print(squ(4))
# squ = lambda : 45
# print(squ())




# global and local scope of var
# global ___ > to local var as a globa var
# a = 45
# def f1():
# 	a =6
# 	print(a)
# def f2():
# 	global a				#6,55,67,67,67
# 	a = 78				#45,45,45,67,67,67
# def f3():				
# 	a = 55				#6,67,67,55,67
# 	print(a)
# def f4():
# 	print(a)
# f4()

# print(a)
# a = 67
# f1()
# print(a)
# f4()
# f2()
# print(a)
# f3()
# print(a)
# f4()






# map(fun,seq) ---------------> it maps in squ depending expressions
# filter(fun,seq) ------------> filrer in the squ depending expressions


# l = [a for a in range(1,21)]

# evn = list(map(lambda a : a%2 == 0,l)) 
# print(evn)
# # print(next(evn))
# # print(list(evn))



# evn = list(filter(lambda a: a%2 == 0,l))
# print(evn)



# recursion
# ---------------


def a():
	for a in range():
		print(a)
	a()
a()

# 998
