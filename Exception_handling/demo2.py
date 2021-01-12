class InsufficientFunds(Exception):
    def __init__(self,arg):
        self.msg=arg
        print(self.msg)
class LimitExceedException(Exception):
    def __init__(self,arg):
        self.msg=arg
        print(self.msg)
class InvalidMinimumException(Exception):
    def __init__(self,arg):
        self.msg=arg
        print(self.msg)
import sqlite3 as s
con = s.connect("Atm.db")
cur = con.cursor()
try:
    cur.execute("create table Accounts(ano number unique ,pin number,balance number ,status message_text )")
except s.OperationalError:
    pass
while True:
    print("-------------------Welcome To ATM-------------------")
    print("1.Create account")
    print("2.Login")
    print("3.Exit")
    choice=int(input("Enter you choice"))
    if choice==1:
        print("Welcome to db bank ")
        print(" kindly set your account details here ")
        try:
            account_number = int(input('Enter your account number'))
            pin = int(input('set your pin'))
            bal = float(input('Enter the amount you want to deposit '))
            cur.execute("""
            insert into Accounts(ano,pin,balance,status)values (?,?,?,?)
            """, (account_number, pin, bal, 'active'))
            con.commit()
            print("user your account is set your details have been saved successfully ")
        except s.IntegrityError:
            print("Username Already taken")
    elif choice==2:
        min_balance =1000.00
        for i in range(3):
            accn = int(input("Enter your account number "))
            cur.execute("select * from Accounts where ano=?", (accn,))
            res = cur.fetchone()
            if res:
                pinnumber = int(input("Enter the pin number"))
                if res[0] == accn and res[1] == pinnumber:
                    if res[3] != 'active':
                        print("sorry your account is blocked visit bank ")
                        break
                    else:
                        print("your available balance is rs ", res[2])
                        while True:
                            print("1.Deposit")
                            print("2.Withdraw")
                            print("3.Logout")
                            option=int(input("Enter an option"))
                            if option==1:
                                amount = float(input("Enter the amount you want to deposit"))
                                if amount>=100:
                                    bal=int(res[2])
                                    bal+=amount
                                    cur.execute("update Accounts set balance=? where ano=?",(bal,accn))
                                    con.commit()
                                    print("Amount ",amount," has been credited in your account ")
                                    cur.execute("select * from Accounts where ano=?", (accn,))
                                    res = cur.fetchone()
                                    print("your available balance is ",res[2])
                                else:
                                    raise InvalidMinimumException("Deposit amount should be greater than 100")
                            elif option==2:
                                amount =float(input("Enter the amount you want to withdraw "))
                                if amount<=10000.00:
                                    if res[2]>amount:
                                        bal=int(res[2])
                                        bal-=amount
                                        if bal>min_balance:
                                            cur.execute("update  Accounts set balance=? where ano=?",(bal,accn))
                                            con.commit()
                                            cur.execute("select * from Accounts where ano=?", (accn,))
                                            res = cur.fetchone()
                                            print("Amount ", amount, " has been debited from your account ")
                                            print("your available balance is ", res[2])
                                        else:
                                            bal+=amount
                                            cur.execute("update  Accounts set balance=? where ano=?", (bal,accn))
                                            con.commit()
                                            raise InsufficientFunds("Insufficient funds")
                                    else:
                                        raise InsufficientFunds("Insufficient funds")
                                else:
                                    raise LimitExceedException("You cannot withdraw beyound 10000")
                            elif option==3:
                                break
                            else:
                                print("please select valid option")
                else:
                    print("invalid pin number")
                    if i != 2:
                        a = input("if you want to continue press yes")
                        if a == 'yes':
                            continue
                        else:
                            break
                    else:
                        cur.execute("update Accounts set status='blocked'where ano=? ", (accn,))
                        con.commit()
                        print("your account is blocked kindly visit bank ")
                        break
        print("thank you")
    elif choice==3:
        break
    else:
        print("please select valid choice")



