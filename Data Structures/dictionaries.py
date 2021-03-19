from sys import getsizeof

# Dictionaries
# Dictionaries can only have immutable keys, but value can be any type
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])

# Get() method returns the value of the given key. If the key dne it returns
# the second argument of the get() method. This method is better than using [] operator
# because if we use [] operator to find a value in dictionary and the key does not exist
# program crashes. To prevent this, we can use get() method.
print(point.get("a", -1))

del point["x"]
print(point)

for key in point:
    print(key, point[key])

# Items() method returns all the key-value pairs as tuples
for key, value in point.items():
    print(key, value)

# We can use comprehensions with both dictionaries and sets.
# Set comprehension
values = {x * 2 for x in range(5)}
print(values)

# Dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)


# Generator expressions
# If we create a comprehension statement with parentheses, it
# becomes a generator expression. This expression creates a generator
# object. Generator objects are iterables, so we can iterate over them.
# These generator object have small sizes. They do not store data at the
# memory so they take little space. But since they do not take space at memory
# we cannot know the len() of the generator object
new_values = (x * 2 for x in range(100000))
print(new_values)
print("gen:", getsizeof(new_values))

new_values = [x * 2 for x in range(100000)]
print("list:", getsizeof(new_values))

# Unpacking operator *. We can unpack any iterable with it
numbers = [1, 2, 3]
print(*numbers)

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1, 2, 3, 4, 5, 6]
second = [7, 8, 9, 10]
combined = [*first, "a", *second]
print(combined)

# To unpack a dictionary use **. If there are same keys, the last key-value
# pair will stay
first_dict = {"x": 1}
second_dict = {"x": 10, "y": 2}
combined_dict = {**first_dict, **second_dict, "z": 22}
print(combined_dict)

# To find the biggest and smallest values we can use max() and min() functions
# as we used with other iterables.
# We can also use values() and key() functions to get the related part pf the
# dictionary
print("max_value:", max(combined_dict.values()))
print("max_key:", max(combined_dict.keys()))
