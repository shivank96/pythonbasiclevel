# to find number of characters,words and lines
# way1
import os,sys
f=open("myfile.txt","w")
text=["Python is a\n","high level\n","programming language\n","that supports oops\n","And it is dynamic typed\n"]
f.writelines(text)
f.close()
alpha=lines=0
word=0
with open("myfile.txt",'r') as f:
    for x in f.read():
        if x==" "or x=="\n":
            word+=1
            if x=="\n":
                lines+=1
        else:
            # x!=" "and x!="\n":
            alpha+=1
print(alpha)
print(word)
print(lines)
# way2
if os.path.isfile("myfile.txt"):
    f=open("myfile.txt","r")
else:
    print("File does not exist:")
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    # words=line.split()
    wcount=wcount+len(line.split())
print("The number of Lines:",lcount)
print("The number of Words:",wcount)
print("The number of Characters:",ccount)
# print(dir(f))
# help(f.writelines)
# for i in range(5):
#     print(i)
#     if i==1:
#         continue
# else:
#     print("bye")