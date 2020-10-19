for x in range(1,11):
    a=5
    print(a,"*",x,"=",a*x)

print("========================")

for x in range(26):
    print(chr(x+65),"---",chr(122-x))

print("========================")

for x in range(5):
    if x==0 or x==4:
        print("*"*5)
    else:
        print("  *")

print("========================")



for i in range(1,5,1):
    print(i,end=" ")

print("\n========================")

for i in range(10):
    print(i,end=" ")

print("\n========================")

for i in range(2,11,2):
    print(i,end=" ")

print("\n========================")

for i in range(10,1):
    print(i,"\n",end=" ")


print("\n========================")

for i in range(10,1,-1):
    print(i,end=" ")

print("\n========================")

for i in range(4,10,-1):
    print(i,end=" ")

print("\n========================")

for i in range(4,10,3):
    print(i,end=" ")

print("\n========================")

for i in range(6,0,-2):
    print(i,end=" ")

print("\n========================")

for i in range(10):
    if i%2!=0:
        print(i,end=" ")

print("\n========================")

sum=0
for i in range(1,6):
    if i%2==0:
        sum=sum+i
print(sum)

print("\n========================")

for i in range(1,6):
    if i%3==0:
        print(i,end=" ")

print("\n========================")

"""n = 10
count = 0
for i in range(n):
    if n%i==0:
        count=count+1
print(count)"""

print("\n========================")

n=5
a=1
for i in range(1,n+1):
    a = a*i
    print(a)

print("\n========================")

x = [2,5,3,6,1,4]
s = 0
for i in x:
    if i%2!=0:
        s = s+i
print(s)

print("\n========================")

for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")

print("\n========================")

for i in range(1,5):
    for j in range(1,i+i):
        print(j,end=" ")
    print()

print("\n========================")
k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k +=1
    print()

print("\n========================")

print("sathya Technology "*5)
print("\n")

print("\n========================")

for x in range(100,0,-1):
    print(x,end=" ")

print("\n========================")
"""
n = int(input("Enter a number:"))
for x in range(n):
    if x%2!=0:
        print(x,"---",x+1)

print("\n========================")

n = int(input("Enter a number:"))
for x in range(5,n,5):
    print(x,end=" ")
"""

print("\n========================")

n = int(input("Enter a number:"))
if n%1==0 and n%n==0:
    print(n,"is the prime number")
