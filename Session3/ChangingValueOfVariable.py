# For the primary data types (int, float, string) you change
# the value of the variable like this
def increment(x):
	return x + 1

x = 5
x = increment(x)
# print(x)


# For lists you can change the value like this
def changeIndexToFive(arr, idx):
	arr[idx] = 5

arr = [1,2]
changeIndexToFive(arr, 1)
# print(arr)


