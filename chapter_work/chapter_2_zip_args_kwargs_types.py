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


# Specify a function that takes arbitrary arguments
def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("named args:", kwargs)

magic(1, 2, key="word", key2="word23")

# Another approach
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}
assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be 6"

# We'll use this syntax to produce higher-order functions whose inputs can accept arbitrary arguments (any arity)
def doubler_correct(f):
    """ works no matter what kind of inputs f expects """
    def g(*args, **kwargs):
        """ Whatever argument g is supplied, pass them through to f """
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6, "doubler supports multiple arity now."
