import mysql.connector as mc
mydb = mc.connect(host="localhost",user="your_username",passwd="your_password",database="Your_database_name")
cur = mydb.cursor()
id = int(input("Enter id"))
cur.execute("DELETE FROM student WHERE sid=%s",(id,))
mydb.commit()