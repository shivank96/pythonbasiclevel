import mysql.connector as mc
mydb = mc.connect(host="localhost",user="your_username",passwd="your_password",database="your_database_name")
cur = mydb.cursor()
cur.execute("CREATE TABLE student(sid integer(4),name varchar(20),emailid varchar(20),phone_num integer(10))")