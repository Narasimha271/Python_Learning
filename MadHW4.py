print('----- Enter Student Details -----\n\n')

name= input("Name: ")
age= int(input("Age: "))
fav_sub= input("Favourite Subject: ")
marks= int(input("Marks Obtained: "))

stud1 = [name, age, fav_sub, marks]

print('----- List -----\n\n')

print(f"Student Details:  {stud1}\n")
print(f"First item: {stud1[0]}\n")
print(f"Last item: {stud1[-1]}\n")
print(f"First 2 item: {stud1[0:2]}\n")
print(f"Last 2 item: {stud1[-2: ]}\n")
print(f"Total items: {len(stud1)}\n")

print('----- Data Types -----\n\n')

print(f"The complete list: {type(stud1)}\n")
print(f"Name: {type(stud1[0])}\n")
print(f"Age: {type(stud1[1])}\n")
print(f"Favourite Subject: {type(stud1[2])}\n")
print(f"Marks: {type(stud1[3])}\n")

fav_sub= 'Python'
stud1[1:3] = [30, "Computer Science"]
stud1[-1:-1] = ["UPSC", "Software Development"]

print(f"Replaced list: {stud1}\n\n")


if marks >= 80:
    result= 'Excellent'
elif marks >= 60:
    result= 'Good'
elif marks>=40: 
    result= 'Pass'
else:
    result='Fail'

print(f"----- Final Output -----\n\n")
print(f"Name: {name} \nAge: {age} \nFavourite Subject: {fav_sub} \nMarks: {marks} \nResult: {result}\n")