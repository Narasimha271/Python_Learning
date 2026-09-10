print('------Reach the Target------\n')

name=input('Name: ')
num=int(input('Give me a starting number: '))

iter = 1

while True:
    if num + 5 >100:
        break
    else: 
        num+=5
        iter+=1
    print(f"{iter}: {num}")

    if iter == 21:
        print('Maximum iterations Reached') 
        break

    
else:
    print('Target reached successfully')

print(f"\nHi {name}! \nFinal Number: {num} \nTotal Iterations: {iter}")