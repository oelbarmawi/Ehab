# Global scope
x = 5

def h(x):
	# This only increments x in the local scope of h
	x = x + 1
	print("Scope h ~", x)

h(x)
# Global variable x only changes with code in the global scope
x += 2
print("Global scope ~", x)

def f():
	# Local scope ~ f
	x = 3

	def g():
		# Local scope ~ g
		print(x+1)

	g()

# f()


