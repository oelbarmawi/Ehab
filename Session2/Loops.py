# For-loop: When you know how many iterations to loop
#		These loops increment for you
# While-loop: Every other type of looping
# 		Need to increment yourself! Do not want infinite loops!

start = 5 
end = 21
skip = 2
for i in range(start, end, skip):
	print('i is:', i)

print("The For-Loop Finished")


i = 0
while i < 10:
	print(i)
	i = i + 1 

print('The while loop finished.')
