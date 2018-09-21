# Function
# ------------

# sytax

# def fucntionname(arguments):
# 	body of the Function


# function defination
# # ---------------------
# def greet():
# 	''' This is a a grating fuction'''
# 	# print('Hello i am in python class')
# 	# return 'I am an returned value from the function'
# 	return 45
# # function call
# # --------------------
# # greet()
# # greet
# # print(greet)
# # greet()
# # print(greet())
# # print(greet.__doc__)


# Arguments
# --------------

# 1.Postional arguments
# 2.default Arguments
# 3.keyword Arguments
# 4.Arbitary length or varable length arguments





# 1.Postional arguments
# ---------------------------

# a = 1
# b = 4
# def add(a,b):
# 	# print(a+b)
# 	return a+b

# # print(add)
# # add(45,675)
# # add('Digital',' Lync')
# add(45.45645,234234234)
# print(add(2,32))



# 2.Default argumets
# ---------------

# def add(a=34,b=56):
# 	print(a+b)
# add()
# add(4)
# add(4,5)



# def add(a,b =67):
# 	print(a+b)
# add(4)


# 3.keyword Arguments
# ---------------------
# def welcome(batan,ironman):
# 	print(batan)
# 	print(ironman)
# welcome(batan = 'USA',ironman = 'India')

# a 
# b` c d e f

# e


# retunindex(lst,elemt)
lst = []
lent = int(input('Enter the length of list\n'))
for a in range(0,lent):
	b = input('Enter the element\n')
	lst.append(b)
print(lst)
elemt = input('Enter the element whose index nu,ber is to be found\n')
def indexreturn(lst,elemt):
	for i in lst:
		if i == elemt:
			return lst.index(elemt)

print(indexreturn(lst,elemt))