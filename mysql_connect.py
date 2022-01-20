import mysql.connector


mydb=mysql.connector.connect(host="localhost",user="root",passwd="8888",database="db1")

mycursor=mydb.cursor()
mycursor.execute("select * from user")
for i in mycursor:
     print(i)