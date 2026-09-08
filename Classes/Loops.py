UserName = input('please enter your name: ')
Magic_Number = int(input('please enter Magic_Number: '))

# While is conditional loop, as far as the condition is true the statements in the while gets executed. after each iteration the condition is checked.
iteration = 1
while Magic_Number < 50:
    print('statement 1')
    Magic_Number +=1
    print(Magic_Number)

    iteration += 1
    if (iteration ==100):
        print('total number of iteratition = '+ iteration)
        break
    
else :
    print('test for else with while')
    
print('Debug')
 
