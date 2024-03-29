# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 02:59:18 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
x = '10'
y = 20
# Convert x to an integer
x_int = int(x)
print(x_int + y)


#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
# Adjust the index to access the last element
print(my_list[my_list_len - 3])


#3
my_string = 'hello world'
# Call the upper method with parentheses to execute it
print(my_string.upper())


#4
z = ['a', 'b', 'c']
z += ['d']
print(z)


#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
x
y = 20
print(x * y)

x = 10
# This will print the value of x, which is 10
print(x)  
y = 20
# This will print the result of x * y, which is 200
print(x * y)  


#6
color = 'My favorite color is {}, what is yours?'.format("blue")
print(color)


#7
color = 'My favorite color is {}, what is yours?'.format("yellow")
print(color)


#8
# Define 'red' as a variable containing the string "red"
red = "red"  
color = f'My favorite color is {red}, what is yours?'
print(color)


#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
# Convert the list to a set to remove duplicates
unique_schools = list(set(schools))
print(unique_schools)


#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
# Convert the tuple to a list 
animals_list = list(animals)
# Replace 'dog' with 'cat'
animals_list[animals_list.index('dog')] = 'cat'
# Convert the list back to a tuple
animals = tuple(animals_list)
print(animals)


#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
# Convert the string to lower-case and then split it into a list of words
words_list = my_sent.lower().split()
print(words_list)














