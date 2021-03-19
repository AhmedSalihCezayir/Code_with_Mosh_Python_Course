print(10 == "10")
print("bag" > "apple")
print("bag" > "BAG")

print(ord("b"))  # This method returns ascii value

temperature = 25
# Indented lines are the ones in the if statement
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature < 20:
    print("It's cold")
    print("It's winter")
else:
    print("NICE")
print("Done")

# Ternary operators
# Both of these are usable
age = 22
message = "Eligible" if age >= 18 else "Not eligible"
# message = ("Not eligible", "Eligible")[age >= 18]
print(message)

# Logical operators and/or/not
# Python also supports short circuit evaluations
high_income = True
good_credit = True
student = False

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if not student:
    print("Not student")
else:
    print("Student")

if ((high_income or good_credit) and not student):
    print("It is working")
else:
    print("Not working")

# Chaning comparison operators
my_age = 22
if 18 <= my_age < 65:
    print("Nice age!")
else:
    print("You are old xd!")

# Ternary operator example
i = False
count = 100
count = count + 1 if (i == True) else (count + 5)
print(count)
