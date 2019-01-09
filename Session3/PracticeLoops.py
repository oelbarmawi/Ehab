def print_names(names):
	"""
	Write a function to print out all of the names in order
	like the following

	names = ["Omar", "Ehab"]

	ouput:
	1. Omar
	2. Ehab
	"""
	length_of_array = len(names)
	for n in range(length_of_array):
		# print(n+1, names[n])
		print("{}. {}".format(n+1, names[n]))




names = ["Omar", "Ehab"]
print_names(names)