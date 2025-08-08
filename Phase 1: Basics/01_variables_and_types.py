# Variables and Data Types in Python

# Integer
age = 25
# Integers are whole numbers, positive or negative, without decimals.
# Secret: Python integers can be arbitrarily large (limited by memory).

# Float
height = 5.9
# Floats are numbers with decimal points.
# Secret: Floats can represent very large or very small numbers, but may lose precision for very long decimals.

# String
name = "Alice"
# Strings are sequences of characters, enclosed in quotes.
# Secret: Strings are immutable (cannot be changed after creation).
# You can use single (' '), double (" "), or triple quotes (''' ''' or """ """).
# You can't change a single character like: name[0] = "M"  # This will give an error

name = "Bob"  # This is allowed! Now 'name' refers to a new string object
print(name)   # Output: Bob

# Boolean
is_student = True
# Booleans represent True or False values.
# Secret: In Python, True is treated as 1 and False as 0 in numeric operations.

# Tuple
coordinates = (10.0, 20.0)
# Tuples are ordered, immutable collections (cannot be changed after creation).
# Secret: Tuples can be used as keys in dictionaries (if all elements are immutable).

bad_key = ([1, 2], 3)  # Contains a list, which is mutable
my_dict = {bad_key: "Error"}  # This will raise a TypeError

# Dictionary
person = {"name": "Alice", "age": 25}
# Dictionaries store key-value pairs, keys must be unique and immutable.
# Secret: Dictionary keys can be any immutable type (string, number, tuple, etc.).
# Access values with person["name"]

# Set
unique_numbers = {1, 2, 3, 2}
# Sets are unordered collections of unique elements.
# Secret: Sets are great for removing duplicates and doing set operations (union, intersection, etc.).

# NoneType
nothing = None
# None represents the absence of a value.
# Secret: None is often used as a default value for function arguments or to indicate 'no result'.

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print(my_dict)

