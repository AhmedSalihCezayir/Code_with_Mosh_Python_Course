import random
import string

# random() returns a value between 0.0 and 1.0
print(random.random())

# randint() returns a value between given numbers(included)
print(random.randint(1, 10))

# choice() returns a random element from the given list
print(random.choice([1, 2, 3, 4]))

# choices() returns a list of random elements. By setting weights= to some list, you can set the weight of each value
print(random.choices([1, 2, 3, 4], k=2))

# We can use choices() method with strings
print(random.choices("abcdefghij", k=4))

# To convert a list to a string, we can use join() method. The first decleared string is the seperator of the values.
print("".join(random.choices("abcdefghij", k=4)))

# We can use string module to get all the letters ana digits
print(string.ascii_letters)
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# To shuffle an array, we can use shuffle method. It changes the original list, it does not return a new list..
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
