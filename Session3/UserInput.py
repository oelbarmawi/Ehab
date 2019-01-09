def getName():
	name = input('What is your name? ')

	print("Your name is {}.".format(name))


# getName()



"""
The function input always returns a string.
"""

def getAge():
	age = input("What is your age? ")

	# To convert a string to an integer [whole numbers]
	my_age = int(age) + 10

	# To convert a string to a float [decimals]
	my_age = float(age) + 10

	print("My age is {}".format(my_age))


getAge()

