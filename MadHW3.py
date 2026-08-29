print('Enter Details')
name=input("Student Name: ")
sub=input("Subject: ")
marks=int(input("Marks Obtained: "))
total = int(input("Total marks: "))
age= int(input("Age: "))
Percentage = marks/total*100

Marks_Lost = total - marks


if age>=18:
    print("Student is an adult")
else:
    print("Student is Minor")

if "Python" in sub:
    print("You are learning Python successfully")

if "Java" not in sub:
    print("Java not found")

print ('-------EXAM Result--------')
print(f"Student: {name}\nAge: {age} \nSubject: {sub} \nMarks: {marks} \nTotal Marks: {total}")
print(f"Marks lost: str({Marks_Lost}) \nPercentage: {Percentage} \nResult: ")
if Percentage>80:
    print("Excellent")
elif Percentage>60:
    print("Good")
elif Percentage>40:
    print("Pass")
else:
    print("Fail")
 
marks+=5
print("Bonus Marks = " + str(marks))
