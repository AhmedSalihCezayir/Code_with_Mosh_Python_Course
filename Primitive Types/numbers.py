import math

# Numbers
x = 1
x = 1.1
x = 1 + 2j  # a + bi (complex number)

print(10 / 3)  # Single slash returns float
print(10 // 3)  # Double slash does integer division
print(10 ** 2)  # Exponential

print("round: " + str(round(2.8)))
print("abs: " + str(abs(-3.5)))

# Import math module first
print("ceil: " + str(math.ceil(3)))  # Returns the smallest int > given one

# Type conversion
x = input("X is :")  # User inputs are always STRING!!
print(type(x))
y = int(x) + 1

print(f"x: {x}, y: {y}")

# You can also convert some values to bool
# "", 0, None => These are Falsy values (They return false)
print("None: " + str(bool(None)))


# Rounds the number entered to the closest multiply of 10
def round10(num):
    return ((num + 5) // 10) * 10


print(round10(15))
