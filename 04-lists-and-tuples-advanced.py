# Difference between two lists
listA = [1, 2, 3, 4]
listB = [1, 2]

difference = []

for elem in listA:
	if elem not in listB:
		difference.append(elem)

print(difference)

# Distance between two 3d points
import math

pointA = [3, 4, 5]
pointB = [1, 3, 5]

addition = ((pointA[0] - pointB[0])**2
			+ (pointA[1] - pointB[1])**2
			+ (pointA[2] - pointB[2])**2)

distance = math.sqrt(addition)

print(distance)
