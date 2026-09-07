print('------Reach the Target------\n')

name=input('Name: ')
num=int(input('Give me a starting number: '))
maxnum=int(input('Target Number: '))

iter = 1

while num<=maxnum:
    print(f"{iter}: {num}")
    num+=5
    iter+=1
    if iter == 11:
        print('Maximum iterations Reached')
        break
else:
    print('Target reached successfully')

num-=5
iter-=1
print(f"\nHi {name}! \nFinal Number: {num} \nTotal Iterations: {iter}")