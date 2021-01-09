import csv
with open("emp.csv",'r') as f:
    res = csv.reader(f)
    data=list(res)
    print(data)
    for line in data:
        for word in line:
            if word=="":
                print("\t\t",end='')
            else:
                print(word,"\t",end='')
        print()
    print("=================================================")
    # printing employee details whose salary is empty
    for line in data:
        if line[2]=="":
            print(line)
    print("=================================================")
    # printing employee details whose salary is greater than 3500
    for line in data:
        if line[2]>'3500':
            print(line)
    print("=================================================")
    # printing employee details whose Name starts with A
    for line in data:
        if 'A' in line[1]:
            res=line[1]
            if res[0]=='A':
                print(line)
    print("=================================================")
    # printing employee details whose details are missing
    for line in data:
        if line[0]=="" or line[1]=="" or line[2] == "":
            print(line)
    print("=================================================")
    # printing employee details whose whose details are complete
    for line in data:
        if line[0]=="" or line[1]=="" or line[2] == "":
            pass
        else:
            print(line)
