# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 03:07:27 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO
#Unless otherwise noted, try solving these using class content and without searching online

#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i == 5:
        i += 1
        # Skip the rest of the loop when i is 5
        continue  
    elif i < 5:
        print('little')
        # This will now only be for i > 5 since i == 5 is handled above
    else:  
        print('big')
    print('Finished!')
    i += 1
    

#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4
    
# Outer loop for each row
# Since the last row is 4, we go up to 5 to include it
for i in range(1, 5):  
    # Inner loop for each number in a row
    # i+1 because the range end is exclusive
    for j in range(1, i + 1):  
        print(j, end=' ')  
        # After finishing a row, print a newline to move to the next row
    print()  
    
    
#3
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list
start_list = [[2, 3, 4], [6, 8, 9]]
flattened_list = []

# Flattening the list
for sublist in start_list:
    for item in sublist:
        flattened_list.append(item)

# Mapping: Subtract 1 from each element
mapped_list = [item - 1 for item in flattened_list]

print(mapped_list)


#4
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end
import datetime

start_dict = {'noah': '2/23/1999', 'sarah':'9/1/2001', 'zach': '8/8/2005'}
converted_dict = {}

for name, date_str in start_dict.items():
    # Convert name to title case
    title_name = name.title()
    # Convert date string to datetime object
    date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
    converted_dict[title_name] = date_obj

print(converted_dict)



 
    
    
    