# Functions
# This function returns None. So even functions that does not return anything returns None
def greet(first_name):
    print(f"Hi {first_name}")


# This function returns a value
def get_greeting(first_name):
    return f"Hi {first_name}"


# Parameter vs argument: arguments are the actual values for the parameters
message = get_greeting("Asude")
print(message)
print(greet("Ahmed"))


# Default arguments should start from the left
def increment(number, by=1):
    return number + by


# Keyword(Named) arguments
print(increment(number=2, by=5))
print("with default argument:", increment(2))


# *args creates tuples. Tuples are iterable
def multiply(*numbers):
    result = 1
    for number in numbers:
        result = result * number

    print(result)
    print(numbers)


multiply(2, 4, 6, 5)


# **args creates dictionary
def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)


def example(*args, **kwargs):
    print(args)
    print(kwargs)


example(1, 2, 3, first=4, second=5)
