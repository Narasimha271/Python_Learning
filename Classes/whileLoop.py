textByUser = input('Give something you want to print: ')

while textByUser.lower() != 'exit':
    print(f'The user given text is: {textByUser.upper()}')
    textByUser = input('please give Next word, you want to print in upper: ')
else:
    print('Thanks!')