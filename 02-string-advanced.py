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

# Check if a string starts with a prefix
s = "Hello"
prefix = "He"

print(s.startswith(prefix))

# Check if a string ends with a suffix
s = "Hello"
suffix = "ello"

print(s.endswith(suffix))

# Reverse words in a string
s = "Hello World"

words_list = s.split(" ")
new_s = ""

for word in words_list:
	reversed_word = "".join(reversed(word))
	swapped_case = reversed_word.swapcase()
	new_s += swapped_case + " "

new_s.rstrip()

print(new_s)

# Count repeated characters
s = "Hello"

repeated_count = 0
repeated_chars = []

for char in s:
	if (s.count(char) > 1) and (char not in repeated_chars):
		repeated_count += 1
		repeated_chars.append(char)

print(repeated_count)

# Sort words in alphabetical order
s = "Hello World"
new_s = ""

words_list = s.split(" ")

for word in words_list:
	new_s += "".join(sorted(word.lower())) + " "

new_s.rstrip()

print(new_s)