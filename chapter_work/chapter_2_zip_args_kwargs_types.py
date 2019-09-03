list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# Zip
pairs = [pair for pair in zip(list1, list2)]

# Unzip
letters, numbers = zip(*pairs)
print(letters)
print(numbers)



## Args
def doubler(f):
    """ Define a function that keeps a reference to f """
    def g(x):
        return 2 * f(x)

    # Return that function
    return g

# This works sometimes
def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3+1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

# But this doesn't work with functions that take more than one argument
def f2(x, y):
    return x + y

g = doubler(f2)

try:
    g(1, 2)
except TypeError:
    print("As defined, g only takes 1 argument.")

