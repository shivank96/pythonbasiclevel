li = [10,50,20,30,20,40,10,40]
for x in li:
    counter = li.count(x)
    if counter>1:
        li.remove(x)
# li.sort()
print(li)