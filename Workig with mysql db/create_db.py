import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="your_username",passwd="your_password")
# database =student is the name of database

#creating a cursor object to establish communication between mysql and python
cur=mydb.cursor(buffered=True)

#execute function is used to execute any of mysql commands in python
#show database and fetchall for it using cur(cursor object) returns all the available list of databases of mysql in list format
cur.execute("show databases")
l = cur.fetchall()
print(l)

#creating a database in mysql using python
cur.execute("CREATE DATABASE practise")

# cur.execute("select * from class1")
# # class1 is the table name which belongs to student database
# res=cur.fetchone()#fetching one record at once
# for i in res:
#     print(i)

