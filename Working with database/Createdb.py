import sqlite3 as s
con = s.connect("products.db")
cur = con.cursor()
try:
    cur.execute("create table Productsinfo(idno number unique ,name message_text ,price number)")
except s.OperationalError:
    pass