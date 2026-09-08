# # Match based condition
# name = input('please enter your name')

# match name:

#     case 'Appu':
#         print('Hi Appu')

#     case 'madhu':
#         print('Hi Madhu')

if (True and 2==2):
    print('hi')    

What_is_the_month_in_numbers = int(input('plese entter this month in number')) 

match What_is_the_month_in_numbers:

    case 1|2:
        print('The month you selected is simha')

    case 9:
        print('The month you selected is Sep')

    case 3:
        print('The month you selected is Mar')

    case 4:
        print('The month you selected is apr')

    case 5:
        print('The month you selected is may')

    case 6:
        print('The month you selected is jun')

    case 7:
        print('The month you selected is jul')

    case 8:
        print('The month you selected is aug')

    case _:
        print('you should have selected in between 1 to 9')


