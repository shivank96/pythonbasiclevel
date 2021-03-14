import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="your_username",passwd="your_password",database="your_database_name")
print(mydb.connection_id)
