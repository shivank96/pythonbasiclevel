name = input("Enter a name ")
print(name.title())
print(name.capitalize())
print(name.upper())
# accepting a input and printing only capital values of that string

name1 = input("Enter a name")
for x in name1:
    if x.istitle():
        print(x)