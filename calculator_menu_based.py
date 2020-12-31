while 1:
    print("-----------Calculator-----------")
    print("================================")
    print()
    print("1. Find Addition")
    print("2. Find Subtraction")
    print("3. Find Multiplication")
    print("4. Find Division")
    print("5. Exit")
    print("Select an option")
    choice = int(input())
    if choice==1:
        print("Enter two numbers ")
        a=int(input())
        b=int(input())
        print("Addition of two numbers is ",a+b)
    elif choice == 2:
        print("Enter two numbers ")
        a = int(input())
        b = int(input())
        print("Subtraction of two numbers is ", a-b)
    elif choice == 3:
        print("Enter two numbers ")
        a = int(input())
        b = int(input())
        print("Multiplication of two numbers is ", a*b)
    elif choice == 4:
        print("Enter two numbers ")
        a = int(input())
        b = int(input())
        print("Multiplication of two numbers is ", a/b)
    elif choice == 5:
        break
    else:
        print("sorry you've choosed wrong option")
        print("please choose a valid option")
    print("Do you want to continue ")
    response = input()
    if response != "y":
        print("------Thank you-------")
        break






