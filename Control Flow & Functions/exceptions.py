from timeit import timeit

# To catch an exception we can use try/except blocks. If there is an exception in the try block
# the program will search for the related exceptions' except block.
# We can also get information related to this exception by given a variable to it.

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except ValueError as ex:
#     print("You didn't enter valid age!")
#     # print(ex)
#     # print(type(ex))
# except ZeroDivisionError:
#     print("Age cannot be zero!")
# else:
#     print("Everthing is fine :)")
# print("Execution continues")


# We can combine exceptions but if there is another expect block after this combined block
# that block will not be executed. That is, after executing one except block, the program
# does not run the other except blocks
try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter valid age!")
else:
    print("Everthing is fine :)")
print("Execution continues")

# If we have any statement after line 33-34, that statement may not be executed because of the
# except block. If there is an exception in line 33-34 the program will go in to the except block.
# So line 38 will not be executed. To solve this problem, we can use finally clause. This finally blok
# always be executed whether there is an exception or not. This block is used to release external resources.
try:
    file = open("exceptions.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter valid age!")
else:
    print("Everthing is fine :)")
finally:
    file.close()
print("Execution continues")

# To automatically release external resources, instead of using finally clause, we can use with statement.
# When we open a file by using with statement, python closes it itself. In other words, with statement is
# used to automatically release external resources.
# If an object has an _exit_ and _enter_ methods, we can use with statement with it. Pyhton will aoutmatically
# call _exit_ methot and it will release external resources. Also by using comma, we can open two files at the
# same time.
try:
    with open("exceptions.py") as file, open("news.txt") as target:
        print("File opened.")
except (ValueError, ZeroDivisionError):
    print("You didn't enter valid age!")
else:
    print("Everthing is fine :)")
print("Execution continues")


# We can throw exceptions by using raise keyword.
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Raising exception is generally more costly. It requires more time to execute the code. Instead of raising exceptions
# we can return a unique value to show there is a problem.
# To see the difference between execution time, we can use timeit function.
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


result = calculate_xfactor(-1)
if result == None:
    pass
"""

# timeit() method takes both the code and the repetition time
print("code1=", timeit(code1, number=10000))
print("code2=", timeit(code2, number=10000))
