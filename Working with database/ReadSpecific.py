import sqlite3 as s
con = s.connect("products.db")
cur = con.cursor()
id = int(input("Enter your id number "))
cur.execute("select * from Productsinfo where idno=?", (id,))
res = cur.fetchone()
print(res)