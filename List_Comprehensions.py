# list comprehension for even values upto n
n=int(input("Enter a number"))
li=[x for x in range(1,n) if x%2==0]
print(li)
# list comprehension for odd values upto n
n=int(input("Enter a number"))
li=[x for x in range(1,n) if x%2!=0]
print(li)
# list comprehension for finding squares of n consecutive number
n=int(input("Enter a number"))
li=[x*x for x in range(1,n+1)]
print(li)
# list comprehension for finding cubes of n consecutive number
n=int(input("Enter a number"))
li=[(x*x*x) for x in range(1,n+1)]
print(li)
