import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["EId","ENAME","ESAL"])
    n=int(input("Enter Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        w.writerow([eno,ename,esal])
print("Total Employees data written to csv file successfully")