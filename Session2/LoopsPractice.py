# Create Triangle
"""
n = 3
*
**
***

n = 5
*
**
***
****
*****

n = 100
*
**
***
....

"""

def create_triangle(n):
	name = "Ehab"
	for i in range(n):
		print("*" * (i + 1))

create_triangle(5) # Calling the function

print("\n\nFizzBuzz")
# FizzBuzz
def fizzbuzz(n):
	
	for i in range(1, n+1):
		if(i % 3 == 0):
			print("fizz")
		elif(i % 5 == 0):
			print("buzz")
		else:
			print(i)
fizzbuzz(10)


print("\n\nSquaredArray")
def squared(arr, size):
	i = 0
	while i < size :
		print(arr[ i ] * arr[ i ])
		i = i + 1

array = [2,4,6,16]
squared(array, len(array))