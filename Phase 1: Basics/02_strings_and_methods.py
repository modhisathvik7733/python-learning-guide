# Strings in Python

# A string is a sequence of characters, enclosed in single, double, or triple quotes.
greeting = "Hello, World!"
single_quote = 'Python'
multi_line = """This is
a multi-line
string."""

# Secret: Strings are immutable. You can't change a character in place.
# greeting[0] = "h"  # This will raise an error

# You can reassign the variable to a new string:
greeting = "Hi, Universe!"

# String concatenation (joining strings)
full_greeting = greeting + " " + single_quote
print(full_greeting)  # Output: Hi, Universe! Python

# String repetition
echo = "ha" * 3
print(echo)  # Output: hahaha

# String indexing and slicing
word = "Python"
print(word[0])    # Output: P (first character)
print(word[-1])   # Output: n (last character)
print(word[1:4])  # Output: yth (characters at index 1,2,3)

# Secret: Slicing never raises an error, even if the range is out of bounds.
print(word[2:100])  # Output: thon

# Common string methods:
text = "  hello, python!  "
text1 = "hello,python,world"

print(text.upper())      # HELLO, PYTHON!
print(text.lower())      # hello, python!
print(text.strip())      # hello, python!   (removes leading/trailing whitespace)
print(text.replace("python", "world"))  #   hello, world!
print(text1.split(","))  # Output: ['hello', 'python', 'world']
print(text.find("python"))  # 9 (index where "python" starts)
print(text.startswith("  he"))  # True
print(text.endswith("!  "))     # True

# Secret: Strings are iterable, so you can loop through each character
for anyVar in "abc":
    print(anyVar)

# Secret: You can use 'in' to check for substrings
print("py" in text)  # True

# Formatting strings (f-strings, recommended in Python 3.6+)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Other formatting options (not recommended for new code):
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))

# Secret: Triple quotes allow multi-line strings and docstrings for functions/classes.
def greet():
    hi = """
    This is a docstring.
    It describes what the function does.
    """
    print("Hello!",hi)

"""main block (any method execution should be done from main usually or can be classed from other method or just normally
   main is used to execute something only when script is run not imported)"""
if __name__ == "__main__":
    greet()


    