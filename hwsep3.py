name = input("Name:")
dayNumber = int(input("Day Number:"))
hoursOfStudy = int(input("Hours of Study:"))

match dayNumber:
    case 1: 
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6| 7:
        print("Weekend")
    case _:
        print("Invalid Day")


subjects = ( "UPSC" , "PYTHON" , "CURRENT AFFAIRS" , "REVISION" )
print("subjects are: ", subjects)
print("First Subject is: ", subjects[0])
print("Last Subject is: ", subjects[-1])
print("Number of Subjects are: ", len(subjects))

subjects = list(subjects)
subjects[-1] = "Practice Questions"
print("Updated Subjects are: ", subjects)

if hoursOfStudy >= 5:
    studyTarget = "Excellent"
elif hoursOfStudy >= 3:
    studyTarget = "Good"
else:
    studyTarget = "Try To Study More"
print("Study Target: ", studyTarget)

print("============== FINAL REPORT ==============")

print(f"Name : {name}")
print(f"Day Number : {dayNumber}")
print(f"updated Subjects : {subjects}")
print(f"Hours of Study : {hoursOfStudy}")
print(f"Study Target : {studyTarget}")

print("================= END =================")

