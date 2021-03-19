# Class: blueprint for creating new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack

class Point:
    # This is a class attribute. This is shared among all instances
    default_color = "red"

    # This method is a constructor. Also this method is a magic method(They start and end with __).
    # Also, self represents the current object.
    def __init__(self, x, y):
        # These are instance attributes. They are unique to each instance
        self.x = x
        self.y = y

    # This magic method is similar to the java's toString() method. When we want to print an object this method
    # is called and if this method is not impelented, it prints the default values (memory location etc.)
    def __str__(self):
        return f"({self.x},{self.y})"

    # This magic method is called when we use == operator.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # This magic method is called when we use > operator.
    def __gt__(self, other):
        return self.x > other.y and self.y > other.y

    # This magic method is called when we use + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # This method is an instance method. We can call it by using an instance of the class. When we want to do
    # something spesifically fot an instance, we use instance methods.
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    # This method is a class method. We call this method using class referance(name). It takes class referance cls.
    # So, we are not working with an individual object. To make this method a class method we need to use "decorator".
    # cls(0, 0) = Point(0, 0)
    @classmethod
    def zero(cls):
        return cls(0, 0)


point = Point(1, 2)
point.draw()

another = Point(3, 4)
another.draw()

# print(type(point))
# print(isinstance(point, Point))

# We can access class attributes by using an instance or just class name. We can also change class attributes
# by using class name(we can also change individual instances class attribute but it does not make sense to change
# a class attribute for an instance)
Point.default_color = "yellow"
print(point.default_color)
print(Point.default_color)

zero_point = Point.zero()
zero_point.draw()

# Without implementing __str__ method, this prints module, followed by class name and the address of this point object
# in memory. However, after we implement __str__ method it prints the returned value from the __str__ method.
print(zero_point)
print(str(zero_point))

# By default equality operator compares referances or addresses of object. To solve this problem we need a magic method
# called __ eq__. To compare our objects, we also need __gt__ or __lt__ magic methods. However, after implementing one of
# them, python automatically implements the other one.
point1 = Point(2, 2)
point2 = Point(2, 2)
point3 = Point(10, 10)

print("point1 == point2:", point1 == point2)
print("point3 > point2:", point3 > point2)
print("point1 + point3", point1 + point3)
