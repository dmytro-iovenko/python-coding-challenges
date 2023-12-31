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

# Print the elements and their indices
my_list = [1, 2, 3, 4]

if not my_list:
	print("Empty List")
else:
	for i, elem in enumerate(my_list):
		print(elem, i)

# Remove matching element
my_list = [3, 3, 2, 1]
elem_to_remove = 3

if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)

print(my_list)

# Remove duplicates from a list
my_list = [1, 1, 2, 3, 4, 4]
no_duplicates = list(set(my_list))
print(no_duplicates)

# Count elements greater than 3
my_list = [1, -1, 0, 2, 2, 3]
count = 0

for elem in my_list:
	if elem > 3:
		count += 1

print(count)

# Find the intersection of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 7, 8, 9}

intersection = set()

for elem in set1:
	if elem in set2:
		intersection.add(elem)

print(intersection)
