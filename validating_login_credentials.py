import sqlite3 as s
con = s.connect("user_credentials.db")
cur = con.cursor()
try:
    cur.execute("create table user_credentials(na message_text unique ,pwd message_text )")
except s.OperationalError:
    pass
name = input('Enter your name ')
password = input('set your password')
try:
    cur.execute("""
    insert into user_credentials(na,pwd)values (?,?)
    """,(name,password))
    con.commit()
    print("user your account is set your details have been saved successfully ")
except s.IntegrityError:
    print("Username already exists")
    pass
resp = input("Do you want to login if yes press y")
if resp=='y':
    for i in range(3):
        username = input("Enter your username ")
        cur.execute("select * from user_credentials where na=?", (username,))
        res = cur.fetchone()
        if res:
            pawd = input("Enter your password")
            if res[0] == username and res[1] == pawd:
                    print("Mr",username," you have logged in successfully ")
                    con.close()
                    print("thank you")
                    break
            else:
                print("invalid credentials ")
                print("please enter valid credentilas ")
                if i != 2:
                    print("you have ",2-i," attempts")
                    a = input("if you want to continue press yes")
                    if a == 'yes':
                        continue
                    else:
                        break
con.close()
