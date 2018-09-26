import sqlite3

conn = sqlite3.connect('pyclass')



# conn.execute('CREATE TABLE classpy1(id int not null ,fname varchar(20),lname varchar(20) , age int, address varchar(50))')
conn.execute('''INSERT INTO classpy1(id,fname,lname,age,address) values(1,'batman','avngers',56,'usa') ''')
conn.commit()
conn.close()