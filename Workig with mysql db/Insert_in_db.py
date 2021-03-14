import mysql.connector as mc
mydb = mc.connect(host="localhost",user="your_username",passwd="your_password",database="your_database_name")
cur = mydb.cursor()
n=int(input("Enter n value"))
id = int(input("Enter id"))
name=input("Enter name")
email = input("Enter emailid")
phone = int(input("Enter phone"))

#inserting one record at a time using execute
cur.execute("INSERT INTO student(sid,name,emailid,phone_num) VALUES(%s,%s,%s,%s)",(id,name,email,phone))

#inserting mutiple records using for loop and execute
for i in range(n):
    id = int(input("Enter id"))
    name=input("Enter name")
    email = input("Enter emailid")
    phone = int(input("Enter phone"))
    cur.execute("INSERT INTO student(sid,name,emailid,phone_num) VALUES(%s,%s,%s,%s)",(id,name,email,phone))

#inserting mutiple records of users given input at a stretch using executemany
li =[]
for i in range(n):
    id = int(input("Enter id"))
    name=input("Enter name")
    email = input("Enter emailid")
    phone = int(input("Enter phone"))
    tu=(id,name,email,phone)
    li.append(tu)
cur.executemany("INSERT INTO student(sid,name,emailid,phone_num) VALUES(%s,%s,%s,%s)",(li))
mydb.commit()