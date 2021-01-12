import sqlite3 as s
con = s.connect("products.db")
cur = con.cursor()
idno = int(input('Enter idno'))
name = input('Enter name')
price = float(input('Enter price '))
cur.execute("""
insert into Productsinfo(idno,name,price)values (?,?,?)
""", (idno,name,price))
con.commit()