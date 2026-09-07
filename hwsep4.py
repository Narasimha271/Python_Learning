name = input("Name: ")
startingNumber = int(input("Starting Number: "))
initialNumber = startingNumber
iterationCount = 1
while startingNumber <= 100:
    

    print(f"currentNumber is: {startingNumber}")
    if (startingNumber == 100):
         print(f"target Number: {startingNumber}")
    iterationCount += 1
    if iterationCount <=20:
        print(f"Iteration Count is: {iterationCount}")
    if (iterationCount == 20):
        print(f"maximum iteration count is Reached: {iterationCount} ")
        print("target Reached Successfully!")
        break 
    startingNumber += 5  
else:
        print(f"maximum iteration count is Reached: {iterationCount} ")
        print("target Reached Successfully!")

print("============== FINAL REPORT ==============")
print(f"Name : hi... {name} !")

print("starting Number is: ", initialNumber)
print(f"Iteration Count : {iterationCount}")
print(f"Target Number is: {startingNumber}")
print(f"maximum iteration count is Reached: {iterationCount} ")
print("target Reached Successfully!")
print("================= END =================")





   

 



