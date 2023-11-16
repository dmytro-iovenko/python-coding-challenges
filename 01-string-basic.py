# Print the length of a string
s = "Python"
print(len(s))

# Print the character at a specific index
s = "Hello"
i = 0

if not s:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i out of range")

# Reverse a string
s = "Hello"

reversed_word = s[::-1]
print(reversed_word)

# Print first and last three characters of a string
s = "Wonderful"
num_chars = 3

if len(s) < 6:
    print("")
else:
    new_string = s[:num_chars] + s[len(s)-num_chars:]
    print(new_string)
