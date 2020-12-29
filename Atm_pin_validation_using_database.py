import sqlite3 as s
con = s.connect("bankpins.db")
cur = con.cursor()
# cur.execute("create table bankaccounts(ano number unique ,name message_text ,pin number ,balance real,status message_text )")
print("Welcome to db bank ")
print(" kindly set your account details here ")
account_number=int(input('Enter your account number'))
na = input('Enter your name ')
pin = int(input('set your pin'))
bal=float(input('Enter the amount you want to deposit '))
cur.execute("""
insert into bankaccounts(ano,name,pin,balance,status)values (?,?,?,?,?)
""",(account_number,na,pin,bal,'active'))
con.commit()
print("user your account is set your details have been saved successfully ")
resp = input("Do you want to login if yes press y")
if resp=='y':
    for i in range(3):
        accn = int(input("Enter your account number "))
        cur.execute("select * from bankaccounts where ano=?", (accn,))
        res = cur.fetchone()
        if res:
            pinnumber = int(input("Enter the pin number"))
            if res[0] == accn and res[2] == pinnumber:
                if res[4] != 'active':
                    print("sorry your account is blocked visit bank ")
                    break
                else:
                    print("Welcome Mr.", res[1])
                    print("your available balance is rs ", res[3])
                    break
            else:
                print("invalid pin number")
                if i != 2:
                    a = input("if you want to continue press yes")
                    if a == 'yes':
                        continue
                    else:
                        break
                else:
                    cur.execute("update bankaccounts set status='blocked'where ano=? ", (accn,))
                    con.commit()
                    print("your account is blocked kindly visit bank ")
                    break
    print("thank you")
