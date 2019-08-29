# Looping
for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
print("done looping")

# Importing modules
import re
my_regex = re.compile("[0-9]", re.I)

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# How to define a function
def double(x):
    """ returns double the input """
    return 2 * x

# Functions are first class, so we can send them as arguments and return functions like expressions
def apply_to_one(f):
    # Applies any supplied function to the number one.
    return f(1)

print(apply_to_one(double))
print(apply_to_one(float))

# We also have lambdas for one line anonymous functions
y = apply_to_one(lambda x: x + 4)
y

# Default arguments are directly defined
def say_hello(name = "World"):
    print("Hello, " + name + "!")

say_hello()
say_hello("Joan")

# We can also specify arguments by name
def full_greeting(greeting = "Hello", name = "World"):
    print(greeting + " " + name + "!")

full_greeting()
full_greeting("Howdy", "Jane")
full_greeting(name="Pat")
full_greeting(greeting="Ahoy")

