from collections import namedtuple

# While working with classes that just have data and not methods, we can use namedtuple class.
# If we dont want to use this class, while comparing our objects, we need the __eq__ method. But if
# we use namedtuple, we dont need to implement that magic method.
Point = namedtuple("Point", ["x", "y"])

# We need to use key-word argument while using namedtuple
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

# We can access the data, but we cannot change it (p1.x = 10 does not work) because namedtuples are immutable.
# But there is a method called _replace() to return another object by changing the values mapped with the passed
# keyname. However, this method does not change the original object.
print("p1._replace(x=22):", p1._replace(x=22))
print(p1 == p2)
