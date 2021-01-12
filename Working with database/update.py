import sqlite3 as s
con = s.connect("products.db")
cur = con.cursor()
id=int(input("Enter id"))
pri=int(input("Enter price"))
cur.execute("update Productsinfo set price=? where idno=?",(pri,id))
con.commit()