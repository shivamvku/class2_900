
# t1 = 12345, 54321, 'hello!'
# t2 = ()
# print(t1)
# print(type(t1))


# print(t2)
# print(type(t2))

t1 = (12,'superman','hell',56.67,9+8j)

# Access el
t2 = 12345, 54321, 'hello!'
# emts in tuples
# index numbers
# print(t[1])
# print(t)

# imnutabable
# ------------------
# t[1] = 'ironman'
# print(t)


# print(t1+t2)
# print(t1*3)

# tuple comphersion

# a = 'DigitalLync'
# b = tuple(a)
# print(b)

# t = [a for a in range(0,11)]
# print(t)
# t = (12,'superman','hell',56.67,9+8j)
# del t[0]

# packed tuples
# ------------------------
 # genarator
 # ------------------
# t = (a for a in range(0,11))
# print(t)
# print(type(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(5*'-')
# for a in t:
# 	print(a)

# iterator
# ----------------

# iter()

sothng = [a for a in range(0,11)]
# print(l)
# t = (12,'superman','hell',56.67,9+8j)
# lt = iter(l)
# tt = iter(t)
# print(type(lt))
# print(type(tt))
# print(lt)
# print(tt)
# print(next(lt))
# for a in lt:
# 	print(a)
# print(60*'-'+'for List ')
# print(next(tt))
# for a in tt:
# 	print(a)


# enumerator
# ---------------------
# import copy
# l1  = ['apple','Nokia','OnePluse',"batman",'superman','ironman']
# print(l1)
# # l2 = l1
# # print(l2)
# # del l2[0]
# # print(l2)
# # print(l1)

# b = copy.copy(l1)
# print(b)
# # print(l2)
# del b[0]
# print(b)
# print(l1)
# enum = enumerate(l)
# print(enum)
# print(type(enum))

# print(next(enum))
# print(next(enum))
# print(40*'-'+'data from loop now')
# for a in enum:
# 	print(a)
# print(next(enum))
# l = []
# for a in enum:
# 	l.append(a)
# print(l)
# l = [a for a in  enum]


l = [1,2,(45,64),7,9]
t = (66,21,[44,4],90,4)
print(l[2][1])
print(t[2][1])
print(l)
l[2][1] = 'cahnged'
print(l)
