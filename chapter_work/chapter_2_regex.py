import re

re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2")
]

assert all(re_examples)


# re.match checks whether the beginning of a string matches a regular expression 
#  while re.search checks if any part of the string matches a regular expression

# see https://docs.python.org/library/re.html
 