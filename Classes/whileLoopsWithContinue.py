UserName = input('please enter your name: ')
Magic_Number = int(input('please enter Magic_Number: '))


# While is conditional loop, as far as the condition is true the statements in the while gets executed. after each iteration the condition is checked.
# A loop is contionous iterations
# Break is used to break the loop
# continue is used to break the iteration

iteration = 1
while Magic_Number < 3:
    if (iteration%5 == 0):
       # print(f'this is a 5th Iteration {iteration}, so we are skipping the Magic number')
        continue

    if (iteration == 21):
        print(f'iteratiton : {iteration}.')
       # break

    print(f'Iteration: {iteration}, the Magic number is {Magic_Number}')
    iteration += 1 #2
    Magic_Number +=1 #2


else :
    print('test for else with while')
   