# from itertools import product

# K, M = map(int, input().split())
# N = []

# for x in range(K):
#     N.append(map(int, input().split()[1:]))
# MAX = -1
# # print(*N)
# for i in product(*N):
#     #print("i:", i)
#     MAX = max(sum(map(lambda x: x**2, i)) % M, MAX)

# print(MAX)

# ---------------------------------------------------------
stri = "Hello"
print(c.upper() for c in stri)


# ---------------------------------------------------------
# A method for making first letter of each word uppercase
def solve(s):
    my_list = list(s)
    my_list[0] = my_list[0].upper()

    for i in range(1, len(s)):
        if s[i - 1] == " ":
            my_list[i] = my_list[i].upper()

    return my_list


print(solve("hello nice people"))


# ---------------------------------------------------------
# A method for reversing elements of a list until the index i(included)
def flip(arr, i):
    new_list = arr[0:i+1][::-1] + arr[i+1:]
    return new_list


my_list = [1, 2, 3, 4, 5, 6]
print(flip(my_list, 3))
