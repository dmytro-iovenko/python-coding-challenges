# Change commas by dots
s = "Hello, World!"
COMMA = ","
DOT = "."

print(s.replace(COMMA, DOT))

# Check if string contains all letters in the alphabet
import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break # Stop the loop immediately

print(is_pangram)

# Remove spaces from a string
s = "Hello, World!"

print(s.replace(" ", ""))
