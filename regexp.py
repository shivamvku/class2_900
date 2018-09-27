# Regular Expression
# =================

# it is a special patter or an expression wich is used
# to extrat,search,find,replae the data from a 
# colltion of string


# How the expression ??

# -----------------------

# r'\d\c' --------- > sample regular expression

# re ------- > re module to perform the regular expression function

# This module exports the following functions:
# =====================================================
# match     Match a regular expression pattern to the beginning of a string.
# fullmatch Match a regular expression pattern to all of a string.
# search    Search a string for the presence of a pattern.
# sub       Substitute occurrences of a pattern found in a string.
# subn      Same as sub, but also return the number of substitutions made.
# split     Split a string by the occurrences of a pattern.
# findall   Find all occurrences of a pattern in a string.
# finditer  Return an iterator yielding a match object for each match.
# compile   Compile a pattern into a RegexObject.
# purge     Clear the regular expression cache.
# escape    Backslash all non-alphanumerics in a string.



# Used to search the charchteres
# -----------------------------------------------------------------------------------
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)

# # r'^\d\d$'
# --------------------------------------------------------------------------------
# Boundary and anchors
# ------------------------------------------------------------
# \ ------ > search single charchtere
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# shivam.vku@gmail.com


# [\w\.\w\]@[\w\.\w]

# ------------------------------------------------------------------
# search gropu of charchteres
# ---__________________________________________________
# []      - Matches Characters in brackets
# [^]    - Matches Characters NOT in brackets

# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
# range of charchteres
# -----------------------------------------
# ( )     - Group

# Quantifiers:
# =======================================================
# *       - 0 or More
# +       - 1 or More------------------> exends


import re

f = open('data.txt','r')
# print(f.read())

a = f.read()
# print(type(a))


# r = re.compile(r'.')
# w = r.finditer(a)

# # print(w)
# # print(next(w))
# # print(next(w))
# # print(next(w))

# for d in w:
# 	print(d)



# searching a single charchtere
# ====================================
# r = re.compile(r'\\\\')
# w = r.finditer(a)
# for d in w:
# 	print(d)



# Search a Group:
# ===============
# r = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# w = r.finditer(a)
# for d in w:
# 	print(d)

# fineding an email
# ====================
# r = re.compile(r'[\w]+\@+[\w\.]+')
# w = r.finditer(a)
# for d in w:
# 	print(d)


r = re.compile(r'\s')
w = r.finditer(a)
for d in w:
	print(d)

# sub(the actual data , repable data,file)

# a = re.sub(r'([\w\.]+\@)+([\w\.]+)' , r'\1digitallync.com' , a)
# print(a)