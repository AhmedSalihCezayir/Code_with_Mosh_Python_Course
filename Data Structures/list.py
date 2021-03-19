# Lists
letters = ["a", "b", "c", "d", "e", "f", "g"]
matrix = [[0, 1], [2, 3]]

# To create a list with multiple same values use * operator
zeros = [0] * 5

# To combine list use + operator. The list do not have to be the same type
combined = zeros + letters

# To create a list up to a number we can use list() function. This functions takes an iterable
numbers = list(range(20))
chars = list("Hello World")

print(zeros)
print(combined)
print(numbers)
print(chars)

# To get the length of the list use len() function
print(len(numbers))

# Accessing list items. It is similar to strings
print(letters[0])
print(letters[-1])

letters[0] = "A"

print(letters[0])
print(letters[0:2])
print(letters[1:])

# We can give step amount
print(numbers[::2])

# Reverse ordered list
print(numbers[::-1])

# List unpacking. The left side needs exact amount of variables to the list's variable amount
new_numbers = [1, 2, 3]
first, second, third = new_numbers
'''
first = new_numbers[0]
second = new_numbers[1]
third = new_numbers[2]
'''

# When we use * before a parameter, python gets all the parameters and pack them into a list
new_list = [1, 2, 3, 4, 4, 4, 4, 4, 9]
start, *middle, last = new_list

print("start:", start)
print("middle:", middle)
print("*middle:", *middle)
print("last:", last)

for number in new_numbers:
    print(number)

# Enumerate() function returns enumerate objects which are iterable. In each iteration it will
# return a tuple. Tuples are like a list but they are read-only. We can unpack the tuple as below.
# These tuples have both the index and the item
for index, number in enumerate(new_numbers):
    print(index, number)
    # print(number[0])

# Adding or removing items
fruits = ["Apple", "Banana", "Mango", "Orange"]

# Append() method adds item to the end of the list
fruits.append("Watermelon")

# Insert() method add item to the given index
fruits.insert(0, "Strawberry")
print(fruits)

# Pop() method removes item from the given index. If index is not given it removes the last item
fruits.pop()
fruits.pop(2)
print(fruits)

# Remove() method removes the given item. It removes the first one it encounter
fruits.remove("Apple")
print(fruits)

# With del statement we can delete range of items at the same time
del fruits[1:3]
print(fruits)

# Clear() method deletes all the items in the list
fruits.clear()
print(fruits)


letters = ["a", "b", "c"]
print("Index of b is:", letters.index("b"))

if "d" in letters:
    print("Index of d is:", letters.index("d"))
else:
    print("There is no 'd' in the list")

print(letters.count("d"))


# Sorting
nice_numbers = [3, 51, 2, 8, 6]
# This method modifies the list
# nice_numbers.sort(reverse=True)

# Use sorted() method to create sorted list without changing the original one
print(sorted(nice_numbers, reverse=False, key=lambda a: abs(a - 20)))
print(nice_numbers)

# List of tuples of two items
order_items = [("Product1", 10),
               ("Product2", 9),
               ("Product3", 12)]

'''
def sort_item(item):
    return item[1]

order_items.sort(key=sort_item)
print(order_items)
'''
# Lambda expression(Anonymous function)
# lambda parameters:expression
order_items.sort(key=lambda item: item[1])
print(order_items)


# Create a new list using lambda expressions and given iterable
'''
prices = []
for item in order_items:
    prices.append(item[1])

print(prices)
'''
# This map() function creates an iterable(map) using the list and the function we gave
# If we iterate through using this iterable, its items are lost. So after we iterate using
# a for loop we cannot use this iterable (e.g if we convert it to a list, this list will be
# empty). So don't use this iterable as it is. Just convert it to a list and then use it.
prices = list(map(lambda item: item[1], order_items))
print(prices)

# You can also pass multiple iterables to a map() function but some conditions are needed.
# For example if your lambda expression returns a sum of 2 values, you can pass 2 iterables,
# so that their elements can be used in the sum
sum_list1 = [2, 4, 6]
sum_list2 = [4, 3, 9]
print(list(map(lambda a, b: a + b, sum_list1, sum_list2)))

# You can also use known functions like int(), abs() etc. with map() function
print(list(map(float, sum_list1)))

# Difference between map() and filter() functions. When we call map with a function, it appends
# the value returned by the function whereas the filter() function appends the values that meet
# the function's condition(it applies the function's filter)
'''
prices = list(map(lambda item: item[1] >= 10, order_items))
print(prices) # This prints (True, False, True)

filtered_list = list(filter(lambda item: item[1], order_items))
print(filtered_list) # This prints the same list as order_items(because there is no actual filtering)
'''

# Like map() function, filter() function also creates an iterable(filter). Because of this we need
# to convert it to a list
filtered_list = list(filter(lambda item: item[1] >= 10, order_items))
print(filtered_list)

# List Comprehension
# [expression for item in items]
# This is same as the map() function
new_prices = [item[1] for item in order_items]
print(new_prices)

# [expression for item in items if condition]
# This is same as the filter() function
# In general do not use the map() and filter() functions. Use list comprehension instead.
new_filtered_list = [item for item in order_items if item[1] >= 10]
print(new_filtered_list)

# Again zip() function returns an iterable(zip). This functions zips the given iterables into
# iterator of tuples
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2, "hey")))
# print(list(map(lambda a, b: (a, b), list1, list2)))

# To find the biggest and smallest values:
print("max:", max(list1))
print("min:", min(list1))

# To find the sum of the values of an int list we can use sum() function
print("sum:", sum(list1))
