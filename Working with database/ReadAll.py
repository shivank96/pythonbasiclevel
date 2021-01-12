import sqlite3 as s
con = s.connect("products.db")
cur = con.cursor()
cur.execute("select * from Productsinfo")
res = cur.fetchall()
for x in res:
    print(x)