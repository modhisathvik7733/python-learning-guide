# Variables and Data Types in Python

# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10.0, 20.0)

# Dictionary
person = {"name": "Alice", "age": 25}

# Set
unique_numbers = {1, 2, 3, 2}

# NoneType
nothing = None


print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# we can have different type in same var as python is dynamically typed no need type conversion

data = 10
print("data of int is:", data)

data = "hello"
print("data as str:", data)

data = 3.5
print("data in float",data)




# List methods examples
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")        # Adds an item to the end
fruits.insert(1, "grape")     # Inserts at index 1
fruits.remove("banana")       # Removes first occurrence of value
fruits.pop()                  # Removes and returns last item
fruits.pop(0)                 # Removes and returns item at index 0
fruits.clear()                # Removes all items
fruits.extend(["kiwi", "melon"]) # Adds all items from another list
fruits.index("kiwi")          # Returns index of first occurrence
fruits.count("kiwi")          # Counts occurrences of value
fruits.sort()                 # Sorts the list in place
fruits.reverse()              # Reverses the list in place
copy_fruits = fruits.copy()   # Returns a shallow copy

print(fruits)

# --- List "Secrets" and Tips ---
# Lists can hold any type:
# mixed = [1, "hello", 3.14, True]

# Negative indexing: Access elements from the end
# fruits[-1] gives the last item

# Slicing: Get sublists easily
# fruits[1:3] gives items at index 1 and 2

# List comprehension: Create lists in one line
# squares = [x*x for x in range(5)]  # [0, 1, 4, 9, 16]

# Membership test: Check if an item exists
# "apple" in fruits  # returns True or False

# Nested lists: Lists can contain other lists
# matrix = [[1, 2], [3, 4]]

# len() function: Get the number of items
# len(fruits)
# --- End of List Tips ---

