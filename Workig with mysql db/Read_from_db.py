import mysql.connector as mc
mydb = mc.connect(host="localhost",user="your_username",passwd="your_password",database="db_name")
cur = mydb.cursor()

#read all records from table using fetchall() function
cur.execute("SELECT * FROM student")
result = cur.fetchall()
for rec in result:
    for val in rec:
        print(val)
    print("------------------")

#read specific record of a table using where clause
id=int(input("Enter id"))
cur.execute("SELECT * FROM student WHERE sid=%s",(id,))
result = cur.fetchone()
for rec in result:
    print(rec)
