
print("please enter your Name: " )
user_name = input()
print("please enter your city Name: ")
user_city = input()
print("please enter your Age: ")
user_Age = int(input())
print ("please enter your Favourate Place to Travel: ")
user_favourate_place = input()
print("please enter Number of Countries You Visited: ")
user_number_of_countries_visited = int(input())
print("Requirements for Travel: ")
requirements_for_travel = str(input())

#Age after 5 years = Current Age + 5

user_Age_after_5_years = int (user_Age + 5)
print(user_Age_after_5_years)

Countries_after_next_trip = int(user_number_of_countries_visited + 1)
print(int(Countries_after_next_trip))


print("--------- TRAVEL PROFILE ---------")

print(f"Hi, {user_name} !")
print(f"you live in {user_city}")
print(f"your favourite place to visit is {user_favourate_place} ")
print(f"you have visited {user_number_of_countries_visited} countries")

print(f"after 5 years your age will be {user_Age_after_5_years} years ")
print(f"after 5 years number of countries you visited will be {Countries_after_next_trip}")

print(user_name +" "+ "is"  +" "+ str(user_Age) + " " + "years old")

print(f" {user_name} is  {user_Age} years old")