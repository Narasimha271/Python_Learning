
print ("================= Exam Result And Eligibility Checker =================")


UserName = input("Name of the Student: ")
SubjectName =input("Enter the Subject Name: ")
MarksObtained = int(input("Enter the Marks Obtained: "))
TotalMarks = int(input("Enter the Total Marks: "))
StudentAge = int(input("Enter the Student Age: "))

percentage = (MarksObtained / TotalMarks) * 100
print("Percentage of the Student is: ", percentage)

Markslost = (TotalMarks - MarksObtained)
print("Marks lost by the Student is: ", Markslost)

if percentage >= 80:
    Result = "excellent performance"
    print("excellent performance")
elif percentage >= 60:
    Result = "good performance"
    print("good performance")
elif percentage >= 40:
    Result = "average performance"
    print("average performance")
elif percentage < 40:
    Result = "Fail"
    print("Fail")
else:
    Result = "Fail"
    print("Fail")

if StudentAge >= 18:
    print("The Student is an adult.")
else:
    print("The Student is a minor.")


contains_python = "python" in SubjectName
if contains_python:
    print("The Subject Name contains the word 'python'. ")
else:
    print("The Subject Name does not contain the word 'python'.")

java_not_present = "java" not in SubjectName
if java_not_present:
    print("The Subject Name does not contain the word 'java'.")


print(" =========== EXAM RESULT AND ELIGIBILITY REPORT =========== ")


print(f"Name of the Student is: ", UserName)
print(f"Age of the Student is: ", StudentAge)
print(f"Subject Name is: ", SubjectName)
print(f"Marks Obtained is: ", MarksObtained)
print(f"Total Marks is: ", TotalMarks)
print(f"Percentage of the Student is: ", percentage)
print(f"Marks lost by the Student is: ", Markslost)
print(f"Result: {Result}")

Bonus_marks= 5
MarksObtained += Bonus_marks
marks_after_bonus = MarksObtained
print("Marks Obtained after Bonus Marks: ", marks_after_bonus)












