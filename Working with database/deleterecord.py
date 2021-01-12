import sqlite3 as s
con = s.connect("products.db")
cur = con.cursor()
id = int(input("Enter idno"))
cur.execute("delete from Productsinfo where idno=?",(id,))
con.commit()