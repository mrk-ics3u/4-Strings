#-----------------------------------------------------------------------------
# Name:        Strings (strings.py)
# Purpose:     Demonstrating string indexes, slices, string methods, looping
#              through strings, comparisons, 'in' and escape characters
#
# Author:      Mr. Kowalczewski
# Created:     28-Sept-2026
# Updated:     28-Sept-2026
#-----------------------------------------------------------------------------

# --- Index -------------------------------------------------------------------
name = "Mr Kowalczewski"

if name == "Mr Kowalczewski":
    print("You have a teacher!")

# accessing individual characters with the index
print(name[9])
print(name[0])
#print(name[20])     # IndexError: there is no index 20

if name[0] == 'M':
    print('M is the first character')

# negative index (backwards from the end)
print(name[-1])
print(name[-3])

# you CANNOT change characters
#name[7] = 'x'

# you CAN do this
name = name + "!"
print(name)

# use a : between index values to access a RANGE (up to, not including, the last value)
print(name[0:8])
print(name[8:10])

# slices work in if statements too
if name[0:2] == 'Mr':
    print('You have a male teacher')


# --- String methods ----------------------------------------------------------
message = "I love Computer Science it's the best!"

# counting characters/strings
print(message.count('e'))

if message.count('e') == 6:
    print("There are 6!")

print(message.count('best'))

# swapping case
print(message.swapcase())

# the original string is NOT modified
print(f"Original string: {message}")

# replacing
print(message.replace('best', 'worst'))
print(message)

# methods that return True or False work in if statements
if message.startswith('j'):
    print('Starts with j')
else:
    print('Does not start with j')

if message.isalpha():
    print('This string is all letters')
else:
    print('There are some non letters')

if message.isupper():
    print("This string is all upper case")

# to keep the change, store the result back into the variable
message = message.swapcase()
print(message)


# --- for loops ---------------------------------------------------------------
# len() gives you the length of a string
name = "Mr Kowalczewski"
print(len(name))

# using range() gives you the index values
for index in range(0, len(name)):
    print(name[index])

# using in stores each character into 'letter' one at a time
for letter in name:
    print(letter)
    if letter == 'z':
        break


# --- Other useful tools ------------------------------------------------------
# what does < mean with strings? (alphabetical order, with a catch)
my_string = "apple"
if my_string < "Hello there":
    print("This string is less than 'Hello there'")

# using 'in' with if statements
name = "Mr Kowalczewski"
if 'z' in name:
    print("There is a 'z' in this name.")

# using escape characters
message = "I love Computer Science.\n\n\nIt is so great.\t\t\t\tIt is my favourite."
print(message)
print("I have:\t\t10 apples.")
