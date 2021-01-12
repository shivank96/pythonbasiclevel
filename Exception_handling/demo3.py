while True:
    print("-----------calculator-----------------")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("Enter your choice"))
    n1 = int(input("Enter a number"))
    n2 = int(input("Enter a number"))
    if choice==1:
        res=n1+n2
        print("sum of two numbers is",res)
    elif choice==2:
        print("difference of two numbers is",n1-n2)
    elif choice==3:
        print("product of two numbers is",n1*n2)
    elif choice==4:
        try:
            res=n1/n2
            print("division result is",res)
        except ZeroDivisionError:
            print("division with zero is not possible")
    elif choice==5:
        break
    else:
        print("please choose valid option")
