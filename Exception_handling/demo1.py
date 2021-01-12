class AttendanceShortageException(Exception):
    def __init__(self,arg):
        self.msg=arg
        print(self.msg)
class IncomeException(Exception):
    def __init__(self,arg):
        self.msg=arg
        print(self.msg)
class GPAException(Exception):
    def __init__(self,arg):
        self.msg=arg
        print(self.msg)
att = int(input("Enter attendance"))
if att>=75:
    income = int(input("Please Enter your annual income"))
    if income<500000:
        gpa = float(input("Enter your gpa"))
        if gpa>=7:
            print("You fulfil all the elgibilty criteria!!!")
            print("You are eligible to apply for scholarship")
        else:
            raise GPAException("You dont have enough gpa sorry you are not eligible to apply for scholarship")
    else:
        raise IncomeException("your income is exceeding 500000 so you are not eligible for scholarship")
else:
    raise AttendanceShortageException("Shortage of attendance your attendance should be atleast 75% to apply for scholarship")
