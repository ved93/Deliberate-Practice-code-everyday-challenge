

# How do you reverse a given string in place?
def main(s):
    # print(len(s))
    # s=s.split()
    s =list(s)
    # print(s)

    for i in range(len(s)//2):

        # print(s[-i], s[i])

        tmp = s[-i-1]
        s[-i-1] = s[i]
        s[i] = tmp

        print(s)
    # print(s[::-1])
    # print("".join(reversed(s)))

    return s


#recursive approach
def reverseString( s, lo=0, hi=None):

    #If one character or less in the string, return the string
    if len(s) <= 1:
        return s

    #The last index should be placed at the end of the string
    if hi == None:
        hi = len(s) - 1

    #If the two indexes cross, return the string
    if hi < lo:
        return s

    #swap the low and high characters
    tmp = s[lo]
    s[lo] = s[hi]
    s[hi] = tmp
    #Recursively call the function
    return reverseString(s, lo + 1, hi - 1)



if __name__ == "__main__":
    print(main("abhishek"))