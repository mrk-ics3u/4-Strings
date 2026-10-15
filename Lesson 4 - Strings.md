# Lesson 4 - Strings

The example code for this lesson is in `strings.py`. Open it alongside these
notes and run it as we go.

We have seen string variables, but have not done much with them besides
printing. This lesson introduces ways to work with strings.

## Index

Think of a string as a list of characters, each with a position number. In
Python (and most languages) the index starts at 0 and is accessed with square
brackets after the variable name.

```python
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
```

## String methods

There are many string methods that do useful things to strings.

```python
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
```

There are many more string methods: https://www.w3schools.com/python/python_ref_string.asp

**Important:** a method that changes a string (like `swapcase()`) does not
change the original. The change only sticks if you store it back into the
variable.

## for loops

A for loop with `range()` iterates through integers one at a time. We can
iterate through a string one character at a time in two ways:

```python
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
```

- `range()` gives you index values, which you then use to get each character.
- `in` gives you each character directly.

## Other useful tools

- `<`, `>` and so on work with strings. What do they tell you?
- `in` can be used in an if statement.
- `\` is the escape character. The character after it has a special meaning:
  `\n` is a new line and `\t` is a tab.

```python
# what does < mean with strings? 
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
```

## Lab

That is it for the lesson. Move on to Lab 4, in `README.md`.
