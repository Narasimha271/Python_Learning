name = input("Name:")
dayNumber = int(input("Day Number 1 to 7:"))
hoursOfStudy = int(input("Hours of Study:"))

match dayNumber:
    case 1: 
        day = 'Monday'
        print("Monday")
    case 2:
        day = 'Tuesday'
        print("Tuesday")
    case 3:
        day = 'Wednesday'
        print("Wednesday")
    case 4:
        day = 'Thursday'
        print("Thursday")
    case 5:
        day = 'Friday'
        print("Friday")
    case 6| 7:
        day = 'Weekend'
        print("Weekend")
    case _:
        print("Invalid Day")


subjects = ( "UPSC" , "PYTHON" , "CURRENT AFFAIRS" , "REVISION" )
print("subjects are: ", subjects)
print("First Subject is: ", subjects[0])
print("Last Subject is: ", subjects[-1])
print("Number of Subjects are: ", len(subjects))
print(type(subjects))

subjects = list(subjects)
subjects[-1] = "Practice Questions"
print("Updated Subjects are: ", subjects)
print(type(subjects))


if hoursOfStudy >= 5:
    studyTarget = "Excellent"
elif hoursOfStudy >= 3:
    studyTarget = "Good"
else:
    studyTarget = "Try To Study More"
print("Study Target: ", studyTarget)

print("============== FINAL REPORT ==============")

print(f"Name : {name}")
print(f"Day : {day}")
print(f"updated Subjects : {subjects}")
print(f"Hours of Study : {hoursOfStudy}")
print(f"Study Target : {studyTarget}")

print("================= END =================")

