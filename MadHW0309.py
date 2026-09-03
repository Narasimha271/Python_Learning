print('----- Enter Student Details -----\n\n')

name= input("Name: ")
age= int(input("Age: "))
fav_sub= input("Favourite Subject: ")
marks= int(input("Marks Obtained: "))

stud1 = [name, age, fav_sub, marks]

print('----- List -----\n\n')

print(f"Student Details:  {stud1}")
print(f"First item: {stud1[0]}")
print(f"Last item: {stud1[-1]}")
print(f"First 2 item: {stud1[0:2]}")
print(f"Last 2 item: {stud1[-2: ]}")
print(f"Total items: {len(stud1)}")

print('----- Data Types -----\n\n')

print(f"The complete list: {type(stud1)}")
print(f"Name: {type(stud1[0])}")
print(f"Age: {type(stud1[1])}")
print(f"Favourite Subject: {type(stud1[2])}")
print(f"Marks: {type(stud1[3])}")

stud1[2]= 'Python'
print(stud1)
stud1[1:3] = [30, "Computer Science"]
print(stud1)
stud1.insert(len(stud1), "UPSC")
stud1.insert(len(stud1),"Software Development")

print(f"Replaced list: {stud1}")


if marks >= 80:
    result= 'Excellent'
elif marks >= 60:
    result= 'Good'
elif marks>=40: 
    result= 'Pass'
else:
    result='Fail'

print(f"----- Final Output -----\n\n")
print(f"Name: {name} \nAge: {age} \nFavourite Subject: {fav_sub} \nMarks: {marks} \nResult: {result}")

print(f"----- Final Output 2 -----\n\n")
print(f"Name: {stud1[0]} \nAge: {stud1[1]} \nFavourite Subject: {stud1[2]} \nMarks: {stud1[3]} \nResult: {result}")