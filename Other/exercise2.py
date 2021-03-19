from pprint import pprint
'''
# My solution
sentence = "This is a common interview question"

letters = {char: 0 for char in sentence}

for char in sentence:
    letters[char] = letters[char] + 1

maxV = 0
for key, value in letters.items():
    if maxV < value:
        maxV = value
        maxK = key
print("Max repeated char is:", maxK)
'''
sentence = "This is a common interview question"
char_freq = {}

for char in sentence:
    if char not in char_freq:
        char_freq[char] = 1
    else:
        char_freq[char] += 1

char_freq_sorted = sorted(char_freq.items(),
                          key=lambda kv: kv[1],
                          reverse=True)
print("Max repeated char is:", char_freq_sorted[0][0])
