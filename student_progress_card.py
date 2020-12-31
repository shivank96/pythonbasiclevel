name=input("Enter your name")
rollno=0
try:
    rollno=int(input("Enter your roll number"))
except ValueError:
    print("Roll number should be of type numbers please enter valid roll no")
    quit()
subjects=['hindi','telugu','english','maths','science','social']
marks=[]
for x in subjects:
    print("Enter marks of subject",x)
    mar = int(input())
    marks.append(mar)
total_marks=0
avg=0
for x in marks:
    total_marks+=x
avg=total_marks/len(marks)
if avg<40:
    print("Mr ", name,"Your roll no is ",rollno)
    print("you are promoted")
    print("you got ", avg, " percentage")
    print("There is no grade for you and your total marks are ", total_marks)
elif avg>=40 and avg<50:
    grade='D'
    print("Mr ",name,"Your roll no is ",rollno)
    print("you got ",avg," percentage")
    print("you got",grade,"grade"," and your total marks are ",total_marks)
elif avg >= 50 and avg < 60:
    grade = 'C'
    print("Mr ", name, "Your roll no is ", rollno)
    print("you got ", avg, " percentage")
    print("you got", grade, "grade", " and your total marks are ", total_marks)
elif avg>=60 and avg<80:
    grade='B'
    print("Mr ", name, "Your roll no is ", rollno)
    print("you got ", avg, " percentage")
    print("you got", grade, "grade", " and your total marks are ", total_marks)
else:
    grade='A'
    print("Mr ", name, "Your roll no is ", rollno)
    print("you got ", avg, " percentage")
    print("you got", grade, "grade", " and your total marks are ", total_marks)
