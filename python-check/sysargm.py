import sys

# total arguments
n = len(sys.argv)
print("total arguments passed :", n)

#arguments passed
print("\n name of the python script:", sys.argv[0]) 

print("\nArguments passed:", end = " ")

for i in range(1, n):

	print(sys.argv[i], end =" ")

###addition of numbers

sum = 0

for i in range(1, n):

	sum += int(sys.argv[i])

print("\n result:", sum)	



