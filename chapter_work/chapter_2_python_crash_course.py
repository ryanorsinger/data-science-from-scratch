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

# Strings
'single quotes are ok'
"double quotes are good 'cause there's a higher likelyhood you'll use a single quotation mark inside a sentence"

#f-strings
greeting = "Hello"
recipient = "World"
full_greeting = f"{greeting} {recipient}"
print(full_greeting)

price = 4.99
message = f"Our best price is ${price} for the appetizer"
print(message)

# Exceptions
try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

# Lists are powerful and mutable
x = [1, 2, 3]
x.extend([3, 4, 5])
x

# Checking if something is in a 
five_is_in_the_list = 5 in [1, 2, 3]
five_is_in_the_list


# Unpacking lists
x, y = [1, 2]
print(x)
print(y)

# Tuples are immutable, yay!
# we can also return a tuple of values from functions
def sum_and_product(a, b):
    return (a + b), (a * b)

sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

# Dictionaries
empty_dictionary = {}
empty_dictionary2 =  dict()
grades = {"joel": 82, "jane": 95}
janes_grade = grades["jane"]

grades_has_jane = "jane" in grades
grades_has_jane

grades["Banjo"] = 100

len(grades)
grades.keys()
grades.values()

# nesting a dictionary
tweet = {
    "user": "ryanorsinger",
    "text": "Data Science is Awesome",
    "retweet_count": 1023,
    "hashtags": ["#data", "#science", "#datascience"]
}

"user" in tweet
"ryanorsinger" in tweet.values()

# DefaultDict is a useful thing

# Setup: imagine we're counting words in a document. With words as keys and the count as the value
document = "Mary had a little lamb, little lamb, little lamb. Mary had a little lamb, its fleece was white as snow"
document = document.split(" ")
document

# Scenario 1: Use an if/else
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
word_counts

# Scenario 2: use a try/except. But this is janky.
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
word_counts

# Scenario 3 is still clunky.
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# Use defaultdict() instead for an approach w/o the logical check or complexity!
from collections import defaultdict
word_counts = defaultdict(int) # in produces 0
for word in document:
    word_counts[word] += 1

word_counts

# Using defaultdict with a list
dd_list = defaultdict(list) # list produces an empty list
dd_list[2] = append(1) # now dd_list is {2: [1]}

# using defaultDict with a dictionary
dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"
dd_dict

dd_pair = defaultdict(lambda: [0, 0]) 
dd_pair[2][1] = 1
dd_pair

# Counters
from collections import Counter
c = Counter([0, 1, 2, 0])
c

word_counts = Counter(document)
word_counts

# A Counter instance has a most_common
for word, count in word_counts.most_common(12):
    print(word, count)

