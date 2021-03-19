from collections import deque
from array import array

# Stacks (LIFO = Last in first out)
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop()
print(last)
print(browsing_session)
print("Redirect:", browsing_session[-1])
if not browsing_session:
    print("Disable button")

# Queues (FIFO = First in first out). We can use dequeue class to implement
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")

# Tuples. Read-only list.
# point = 1,
point = 1, 2
print(type(point))

evens = (2, 4)
odds = (3, 5)
numbers = evens + odds
print(numbers)

# You can use * operator to repeat the values in a tuple
print(evens * 2)

names = tuple(["John", "Karen", "Helen"])
print(names)
print(names[0:2])

# Unpacking
x, y, z = names
print(y)

if "Helen" in names:
    print("Exists")

# Cannot modify items
#names[0] = "Mike"

# Swapping items using tuples. As we know, the right side of the expression is a tuple
# and at the left side we are unpacking it
x = 10
y = 11
x, y = y, x
print(f"x: {x}, y: {y}")

# By using this, we can define multiple variables at the same line
a, b = 1, 2
print(f"a: {a}, b: {b}")

# Arrays. Use arrays when you are working with large amounth of numbers to
# solve performance problems. In other cases, use lists and tuples.
# Array stores same type items which is determined by the type code given to
# the array() method.
numbers = array("i", [1, 2, 3])
print(numbers)

# Sets are collections with no duplicates. They are unordered so we cannot
# access its items with []
random_numbers = [1, 1, 2, 3, 4, 4]
first = set(random_numbers)
second = {1, 5}
# second.add(5)
# second.remove(4)
# print(len(second))

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

if 1 in first:
    print("Yes")
