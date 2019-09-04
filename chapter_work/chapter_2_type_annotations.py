# Python is a dynamically typed language

def add(a, b):
    return a + b

assert add(10, 5) == 15, "+ is valid for numbers"
assert add([1, 2], [3]) == [1, 2, 3], "+ is valid for lists"
assert add("hi ", "there") == "hi there", "+ is valid for strings"

try:
    add(10, "five")
except TypeError:
    print("Cannot add an integer to a string")

# Example of static typing
def add(a: int, b: int) -> int:
    return a + b

add(10, 5)
add("hi, ", "there")

# Four reasons to use type annotations
# 1 - Types are an important form of documentation
# 2 - Code introspection before we run the code
# 3 - Having to think about types forces you to design cleaner functions and interfaces
# 4 - Using types allows your editor to help with things like autocomplete (tooling assistance)

# Consider the difference
# def dot_product(x, y): ... 
# vs.
# def dot_product(x: Vector, y: Vector) -> float:

# from typing import Union
# def secretly_ugly_function(value, operation): ...
# def ugly_function(value: int,
#                   operation: Union[str, int, float, bool]) -> int:


from typing import List # not the capital L

def total(xs: List[float]) -> float:
    return sum(total)



from typing import Optional
values: List[int] = []
best_so_far: Optional[float] = None # allowed to be a float or None

from typing import Dict, Iterable, Tuple

# Keys are strings, values are ints
counts: Dictt[str, int] = {"data": 1, "science", 2}

if lazy:
    evens: Iterable[int] = (x for x in range 10 if x % 2 == 0)
else:
    evens = [0, 2, 4, 6, 8]


# Tuples specify a type for each argument
triple: Tuple[inint, float, int] = (10, 2.333, 5)

from typing import Callable

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints") == "type hints, type hints"

Number = int
Numbers = List[Number]

def total(xs: Numbers) -> Number:
    return sum(xs)

