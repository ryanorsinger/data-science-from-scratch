def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in generate_range(10):
    print(f"i: {i}")

## With a generator, we can create an infinite sequence

def natural_numbers():
    """ returns 1, 2, 3, ..., n """
    n = 1
    while True:
        yield n
        n += 1
        
natural_numbers()

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)

import random
random.seed(23) # set the seed to 23

four_uniform_randoms = [random.random() for _ in range(4)]
four_uniform_randoms

random.seed(23) # reset the seed to 23
print(random.random())
random.seed(23) # reset the seed to 23
print(random.random())
# Setting seeds allows us to get reproducible results

random.randrange(10)
random.randrange(3, 6)

up_to_ten = list(range(10))
up_to_ten
random.shuffle(up_to_ten)
print(up_to_ten)

captains = ["Archer", "Kirk", "Piccard", "Sisko", "Janeway"]
random_captain = random.choice(captains)
random_captain

# Sample with NO DUPLICATES
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
winning_numbers

# Sample with replacement if OK with duplicates
four_with_replacements = [random.choice(range(10)) for _ in range(4)]
four_with_replacements

