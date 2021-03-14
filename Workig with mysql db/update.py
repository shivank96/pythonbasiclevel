import mysql.connector as mc
mydb = mc.connect(host="localhost",user="your_username",passwd="Your_password",database="your_database_name")
cur = mydb.cursor()

#update a record
phone = int(input("Enter phone number"))
id = int(input("Enter id"))
cur.execute("SELECT * FROM student WHERE sid=%s",(id,))
result = cur.fetchone()
print("Before updating")
for i in result:
    print(i)
cur.execute("UPDATE student SET phone_num=%s WHERE sid=%s",(phone,id))
mydb.commit()
cur.execute("SELECT * FROM student WHERE sid=%s",(id,))
result = cur.fetchone()
print("After updating")
for i in result:
    print(i)