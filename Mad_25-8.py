print('\n\nWelcome to Cheema Narasimha Howla Tours & Travels')
print('\nPlease enter your details to proceed with the booking.\n')
Name= input('Name: ')
City= input('City: ')
Age= input('Age: ')
Age_int= int(Age)
FavPlace= input('Favorite Place to Travel: ')
CountriesVisited= input('How many Countries have you visited so far? : ')
CountriesVisited_int= int(CountriesVisited)
Requirements= input('Any special requirements for your trip? : ')

NewAge= Age_int + 5
NewCountriesVisited= CountriesVisited_int + 1

print(f'\n\nHi {Name}!\n\nYou live in {City}.\nYou are {Age_int} years old.\nYour favorite place to travel is {FavPlace}.\nYou have visited {CountriesVisited_int} country(s) so far.\nSpecial requirements: {Requirements} \nAfter 5 years, you will be {NewAge} years old.\nAfter your next trip, you will have visited {NewCountriesVisited} countries.')

input('\n\nReady for the EXTRA CHALLENGE?\n') 
print('\n'+ Name + ' is ' + Age + ' years old.')  

input('\n\nReady for the last challenge? \n')

print('\nCHALLENGE ACCEPTED!\n' + Name + ' is ' + str(Age_int) + ' years old.') #Converting int to string + concatenate