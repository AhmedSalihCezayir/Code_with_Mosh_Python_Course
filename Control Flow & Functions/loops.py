# Loops
for number in range(3):
    print("Attempt", number + 1, "." * (number + 1))

for number in range(1, 4):
    print("Nice", number, "." * number)

for number in range(1, 10, 3):
    print("Number:", number)

# For else statement. If we break out of loop else part does not work
successful = True
for number in range(3):
    print("Attempt", end=" ", flush=True)
    if successful:
        print("Successful")
        break
else:
    print()
    print("Attempted 3 times and failed")

# Nested loops
for i in range(5):
    for k in range(3):
        print(f"({i},{k})")

print("5:", type(5))
print("range(5):", type(range(5)))

# Range, strings and lists are iterable
for c in "Python":
    print(c)

for a in [1, 4, 6, 3]:
    print(a)

# While loop
number = 100
while number > 0:
    print(number)
    number //= 2

# Do while loopish while loop
while True:
    command = input(">>>")
    if (command.lower() == "quit"):
        break
    print("Echo:", command)

count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"We have {count} even numbers")
