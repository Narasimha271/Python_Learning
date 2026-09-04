print('-----Enter Your Details-----')
name=input('Name: ')
day_num= int(input('What day of the week is it (between 1-7): '))
stud_hours=int(input('How many hours are you planning to study (in hours): '))

match day_num : 
    case 1:
     day='Monday'

    case 2:
     day='Tuesday'

    case 3:
     day='Wednesday'

    case 4:
     day='Thursday'

    case 5:
     day='Friday'

    case 6:
     day='Saturday'

    case 7:
     day='Sunday'


#3. Study Subjects
subs = ("UPSC, Python, Current Affairs, Revision")

print(subs)
print(len(subs))
print(subs[0])
print(subs[-1])

subs_list = list(subs)
subs_list[-1] = 'Practice Questions'

print(subs_list)

#Study Target

if stud_hours >=5:
    target='Excellent target'
elif stud_hours >=3:
    target='Good target'
else:
    target='Try to study a little more'

#Final Report
print(f"Student: {name}")
print(f"Day: {day_num}")
print(f"Study Hourse: {stud_hours}")
print(subs_list)
print(f"Number of Subjects: {len(subs_list)}")
print(f"Study Target: {target}")