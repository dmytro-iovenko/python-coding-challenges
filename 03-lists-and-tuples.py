# Multiply all elements in a list
my_list = [3, 4, 5, 6]
factor = 2

for i in range(len(my_list)):
	my_list[i] *= factor

print(my_list)

# Print elements on the same line without commas
my_list = [3, 4, 5, 6]

for elem in my_list:
	print(elem, end=" ")

# Get max and min values
my_list = [3, 4, 5, 6]

if my_list:
	print(max(my_list), min(my_list))
else:
	print(None)

# Check if list is empty or not
my_list = [4, 5, 6, 7]

if len(my_list) == 0:
	print("Empty")
else:
	print("Not Empty")
