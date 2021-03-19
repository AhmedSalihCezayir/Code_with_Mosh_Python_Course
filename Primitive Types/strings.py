print("Hello World")
print("*" * 10)  # (string * int) gives multiple strings appended to eachother

# If you want to seperate your values with something different from a space specify a sep=
print(1, 2, 3, 4, 5, sep=";;")

# If we want to continue with the same line after printing one you need to specify end=
print("a", "b", "c", "d", end=""),

isPublished = True  # Boolean values starts with uppercase

# Three quote (single or double) for saving format
string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# Strings (You can also use single quotes)
course = "Python Programming Course"
print(len(course))  # Length of the string
print(course[0])  # Like charAt
print(course[-1])  # Works with negative values. -1 gives the last char
print(course[0:3])  # Substring (last index is exclusive)
print(course[0:])  # From given index to end substring
# From start to given index substring (last index is exclusive)
print(course[:3])
print(course[:])  # All string

# Escape sequences \' \" \\ \n
first_course = "'Python Classes'"
second_course = "\"Python Classes\""
first_string = "First \nSecond"  # Space after the escape sequence is important

print(first_course)
print(second_course)
print(first_string)

# Formatted strings
first = "Ahmed"
second = "Salih"
full_name = first + " " + second
formatted_full_name = f"{first} {second} {2 + 2}"  # f-strings
print(formatted_full_name)

# String methods
method_string = "python programming"
bad_string = "      bad string  "

print(method_string.upper())  # There is also lower() method
print(method_string.title())  # Capitalizes first letters
print(method_string.find("thon"))  # Returns the index / -1 if DNE
print(method_string.replace("p", "j"))  # Replaces each instance
print(method_string)  # Strings are immutable so it does not change
print("pyt" in method_string)  # Returns boolean value
print("jojo" not in method_string)

print("\n")

print(bad_string)
print(bad_string.strip())  # Removes the spaces that are at the beginning / end
print(bad_string.lstrip())  # Removes the spaces that are at the beginning
print(bad_string.rstrip())  # Removes the spaces that are at the end

repeated_string = "hellohellohello"
nice_string = "llo"
print("hello count: ", repeated_string.count("hello"))
print("s1 ends with s2:", repeated_string.endswith(nice_string))
