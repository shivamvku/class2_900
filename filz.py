# # open()

# # f  = open('finamame.ext','mode',encoding)

# # encoding
	
# # 	utf -8
# # 	utf -16

# # # utf --- unicode text format - 8(decryption ) 

# # f.close()

# # example ------- 1
# # ====================

# # f = open('sample.txt','w')
# # f.close()

# # creating a file in an onther dir
# # f = open('/home/vineet/Documents/vineet/python/classs2_900/demo_pkg/demo.txt','w')
# # f.close()



# # writing data into my file
# # =====================================
# # f = open('sample.txt','a')
# # # f.write('This is my first line\n')
# # # f.write('This is my second line\n')
# # f.write('this is my 3 rd lie\n')
# # f.close()



# # Read DATA  from file
# # ==============================================
# # f = open('sample.txt','r')
# # # print(f.read())
# # # print(f.read(6))
# # print(f.readline())
# # print(f.tell())
# # # print(f.readline(5))
# # f.seek(1)

# # print(f.readline())

# # f.close()

# # # cursors methods
# # # ===================================
# # # offset --- 
# # # 			0 ------- rows 
# # # 			1 ------- coloums
# # # .seek(char,offset) -----> move your cursors to deseid postion
# # # .tell() ---------> Will give current postion of the cursors

# # f = open('sample.txt','r')
# # print(f.tell())
# # print(f.read())
# # print(f.tell())
# # print(60*'-')
# # f.seek(22)
# # print(f.tell())
# # print(f.read())
# # print(f.tell())
# # print(60*'-')
# # print(f.tell())
# # print(f.seek(0,0))
# # print(f.tell())
# # print(f.read())
# # print(f.tell())
# # f.close()




# # working with Dictories
# # ==============================

# import os

# # os.mkdir('dummydir')
# # os.mkdir('/home/vineet/Documents/vineet/python/classs2_900/dummydir/indummy')


# # os.rmdir('/home/vineet/Documents/vineet/python/classs2_900/dummydir/indummy')
# # os.rmdir('dummydir')
# # os.rmdir('indumy')



# # print(os.getcwd())

# # os.chdir('/home/vineet/Documents/vineet/python/classs2_900/dummydir/indummy')

# # print(os.getcwd())



# #  woring only with files
# # =====================

# # # os.remove('/home/vineet/Documents/vineet/python/classs2_900/sample.txt')

# # # print(os.path.getsize('/home/vineet/Documents/vineet/python/classs2_900/demo_pkg'))


# # =====================
# # CSV file
# # ===================

# # reader(...)
# #         csv_reader = reader(iterable [, dialect='excel']
# #                                 [optional keyword args])
# #             for row in csv_reader:
# #                 process(row)



# # writer(...)
# #         csv_writer = csv.writer(fileobj [, dialect='excel']
# #                                     [optional keyword args])
# #             for row in sequence:
# #                 csv_writer.writerow(row)
        


import csv

# def pen(fileobj,data):

# 	wr = csv.writer(fileobj,delimiter=',')
# 	print(wr)
# 	print(data)
# 	for a in data:
# 		wr.writerow(a)


# def rread(fileobj):

# 	rw = csv.reader(fileobj,delimiter = ',')
# 	print(rw) 
# 	# print(next(rw))
# 	# print(next(rw))

# 	for a in rw:
# 		print(a)

def rread(fileobj):

	rw = csv.DictReader(fileobj,delimiter = ',')
	print(rw) 
	# print(next(rw))
	# print(next(rw))

	# for a in rw:
	# 	print(a)



if __name__ == '__main__':

	# fileobj = open('sample.csv','w')

	# data = [

	# 		'fName,lName,age,address'.split(','),
	# 		'Batman,avnger,50,usa'.split(','),
	# 		'superman,avnger,50,usa'.split(','),
	# 		'ironman,avnger,50,usa'.split(','),
	# 		'wonderwomen,avnger,50,usa'.split(','),
	# 		'khali,avnger,50,usa'.split(','),


	# 		]

	# pen(fileobj,data)

	fileobj = open('sample.csv','r')
	rread(fileobj)

	fileobj.close()




person ---- 1

name : 'Batman'
age : 50 


person ----- 2


