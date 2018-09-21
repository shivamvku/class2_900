# a = {'apple',(45,67,4),22,56.89,6+8j}

# print(a)

# a.update([2,3,4,22])

# print(a)

# a1 = {3,4,5,67,32,12,455,11,5542,12131,7,4,223,23,54,5}
# a2 =  { 67,3.54,67.7,3,5,223}


# intersection
# ---------------------------------
# print(a1.intersection(a2))
# print(a1&a2)


# # union
# # ---------------------

# print(a1|a2)
# print(a1.union(a2))



# print(a1-a2)
# print(a2-a1)


# print(a1.symmetric_difference(a2))

# print(a2.symmetric_difference(a1))



# a  = {1,2,3}
# b = {1,2,3}
# print(a.symmetric_difference(b))


# frozenset()
# -------------------

a = {1,2,3,4}#----------> superset
b = {3,4}#----------> subset
# c= [4,5,6,7,4,3,2,1,3]
# d = (45,22,67,45,21,6)

# fz1 = frozenset(a)
# fz2 = frozenset(b)
# fz3 = frozenset(c)

# fz4 = frozenset(d)
# print(fz1)
# print(fz2)

# print(fz3)

# print(fz4)

# issubset()
# issuperset()


# a < b
# a -------  subet
# b ------ superset

# print(a.issuperset(b))
# print(b.issuperset(a))

# print(a.issubset(b))
# print(b.issubset(a))

l = 