print("==============PERSONAL PROFILE ==============")
UserName = input("Name : ")
UserAge = int(input("Age : "))
UserFavouriteSubject = input("Favourite Subject : ")
MarksObtained = int(input("Marks Obtained : "))

PersonalDetails = [UserName, UserAge, UserFavouriteSubject, MarksObtained]
print("Personal Details of the Student are: ", PersonalDetails)
print(PersonalDetails[0])
print(PersonalDetails[-1])
print(PersonalDetails[0:2])
print(PersonalDetails[-2: ])
print(len(PersonalDetails))

print(type(PersonalDetails))
print(type(PersonalDetails[0]))
print(type(PersonalDetails[1]))
print(type(PersonalDetails[2]))
print(type(PersonalDetails[3]))
PersonalDetails[2] = "Python"
print(PersonalDetails)
PersonalDetails[1] = 30
print(PersonalDetails)
PersonalDetails[2] = "Computer Science"
print(PersonalDetails)

PersonalDetails[1:3] = "30", "Programming Language And Computer Science"
print(PersonalDetails)
PersonalDetails[-1:-1] = "UPSC CIVIL SERVICES", "SOFTWARE DEVELOPMENT"
print(PersonalDetails)

if MarksObtained >= 80: 
 print("excellent")
elif MarksObtained >= 60:
    print("good")
elif MarksObtained >= 40:
    print("average")
else:
    print("Fail")

print("==============PERSONAL PROFILE REPORT ==============")
print(f"Name : {UserName}")
print(f"Age : {UserAge}")
print(f"Favourite Subject : {UserFavouriteSubject}")
print(f"Marks Obtained : {MarksObtained}")
print(f"Result : {(MarksObtained/100)*100}")
print("================= END =================")



