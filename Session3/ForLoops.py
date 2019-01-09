# There are two ways to write For-Loops

# The first way
# For doing a task a set amount of times.
for i in range(10):
	print(i)

print("\n")

# The second way
# Iterating through a list/array/collection of data

colors = ["blue", "green", "orange"]
for color in colors:
	print(color)

print("\n")

# Mixing both of these
length_of_array = len(colors) # length_of_arrays = 3
for i in range(length_of_array):
	print(i, colors[i])

