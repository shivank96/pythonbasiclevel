import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="your_user_name",passwd="your_password",database="Student")
# database =student is the name of dataase
cur=mydb.cursor()
# cur.execute("show databases")

cur.execute("select * from class1")
# class1 is the table name which belongs to student database
res=cur.fetchone()#fetching one record at once
for i in res:
    print(i)