# even numbers upto n
def Even_numbers(n):
    li = [x for x in range(1,n+1) if x%2==0]
    for x in li:
        print(x,end=" ")
    print()
def Odd_numbers(n):
    li = [x for x in range(1,n+1) if x%2!=0]
    for x in li:
        print(x,end=" ")
    print()
def table_of_a_number(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
def max_of_numbers(*n):
    maxi = 0
    for x in n:
        if x>maxi:maxi=x
    print("maximum value is ",maxi)
def max_of_numbers_in_a_list(li):
    maxim=0
    for x in li:
        if x>maxim:
            maxim=x
    print("maximum value in the list ",maxim)
def min_of_numbers_in_a_tuple(tup):
    mini=min(tup)
    print("maximum value in the list ",mini)
def factorial_of_number(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial of ",n," is ",fact)
Even_numbers(10)
Odd_numbers(20)
table_of_a_number(5)
max_of_numbers(25,40)
max_of_numbers(45,10,65)
max_of_numbers()
lis=[33,44,22,55,12]
max_of_numbers_in_a_list(lis)
tupl=(22,11,55,21,68)
min_of_numbers_in_a_tuple(tupl)
factorial_of_number(4)