
def gcd(a,b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
  
# function return number
# which divides these
# three number and leaves
# same remainder .
def sameRemainder(a,b,c):
 
    # We find the differences
    # of all three  pairs
    a1 = (b - a)
    b1 = (c - b)
    c1 = (c - a)
  
    # Return GCD of three differences.
    return gcd(a1, gcd(b1, c1))
 
# Driver program
 
a = 62
b = 132
c = 237
print(sameRemainder(a, b, c))