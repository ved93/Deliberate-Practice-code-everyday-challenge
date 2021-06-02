# https://www.geeksforgeeks.org/largest-number-less-than-or-equal-to-z-that-leaves-a-remainder-x-when-divided-by-y/

# https://www.quora.com/How-do-you-write-a-Python-program-if-you-are-given-three-numbers-a-b-and-c-Write-a-program-to-determine-the-largest-number-that-is-less-than-or-equal-to-c-and-leaves-a-remainder-b-when-divided-by-a
# Python implementation to Find the
# largest non-negative number that
# is less than or equal to integer Z
# and leaves a remainder X when divided by Y

# Function to get the number
def get(x, y, z):
	
	# remainder can't be larger
	# than the largest number,
	# if so then answer doesn't exist.
	if (x > z):
		return -1
		
	# reduce number by x
	val = z - x
	
	# finding the possible
	# number that is divisible by y
	div = (z - x) // y
	
	
	# this number is always <= x
	# as we calculated over z - x
	ans = div * y + x
	
	return ans


# Driver Code
# initialise the three integers
x = 1
y = 5
z = 8

print(get(x, y, z))

# This code is contributed by shubhamsingh10
