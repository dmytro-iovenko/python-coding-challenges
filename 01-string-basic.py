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

# Remove characters at even indices
s = "Coding"
new_s = ""

for i in range(len(s)):
    if i % 2 != 0:
        new_s += s[i]

print(new_s)

# Check if a string only contains numbers
s = "Hello59"

print(s.isdecimal())

# Remove character from a string
s = "Hello"
n = 1

if (len(s) == 0) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)

# Replace a character in a string
s = "Hello"

curr_char = "l"
new_char = "s"

print(s.replace(curr_char, new_char))
