
# In Python There are 4 types of collections
# 1) List
# 2) Tuple
# 3) Set
# 4) Dictonary 

# List - List is a collection of objects, that is of either same type or different type
# 
# ListName = [obj1, obj2, obj3] 


fruits_i_eat = ["Apples", "Oranges", "Kiwi"]

print(fruits_i_eat[1])

# Len() function is used to identify the lenth of the list
print(len(fruits_i_eat))

print(len(fruits_i_eat[1]))

Me = ["Simha", 3500, 1.5, True]

print(Me[1])

Me[1] = "test"
print(f'line 27: {Me}')

Me[1:3] = ["Appu", 'Madhu']

print(f'line 31: {Me}')

Me[1:2] =  ["Appu", 'Madhu']

print(f'line 35: {Me}')


Me[0:0] =  ["Dippu", 'Mahesh']

print(f'line 40: {Me}')

Me[-1:-1] =  ["nani", 'arun']

print(f'line 44: {Me}')

Me[-2:-2] =  ["Sai", 'Pandu']

print(f'line 48: {Me}')

print(Me[1])

print(Me[-1])

print(Me)
Me.insert(len(Me), "Sep 02")
print(Me)

list1 = ["apples", "kiwi", "oranges"]
list2 = ["carrots", 'potatoes', 'fish']
list1.extend(list2)
list2.extend(list2)

print(list2)