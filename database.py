# class2_900

# import pymysql
# con = pymysql.connect('localhost','root','mysqlpassword','class2_900')
# con.close()




# import pymysql

# con = pymysql.connect('localhost','root','mysqlpassword','class2_900')
# cur = con.cursor()
# var = '''CREATE TABLE classpy1(id int not null ,fname varchar(20),lname varchar(20) , age int, address varchar(50)); '''
# cur.execute(var)
# con.close()







# import pymysql

# con = pymysql.connect('localhost','root','mysqlpassword','class2_900')
# cur = con.cursor()
# var = '''INSERT INTO classpy1(id,fname,lname,age,address) values(1,'batman','avngers',56,'usa') '''
# cur.execute(var)
# con.commit()
# con.close()






import pymysql

con = pymysql.connect('localhost','root','mysqlpassword','class2_900')
cur = con.cursor()
q = cur.execute(''' SELECT * FROM classpy1''')
print(q)
data = cur.fetchall()
# print(data)

for a in data:
	print(a)
	
con.close()



