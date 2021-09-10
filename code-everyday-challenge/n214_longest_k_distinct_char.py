

def longest_substr_distinct_char(s):

    u = ''
    prev_longest = '' 
    for i, char in enumerate(s):
        if char in u:
            ind = u.index(char)
            # print(u[ind+1:])
            u = u[ind+1:]+char
        else:
            u = u+char

        if len(prev_longest) < len(u):
            prev_longest = u



    return u,len(prev_longest)



#sliding method
def longestUniqueSubsttr(string):
      
    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0
  
    # starting the initial point of window to index 0
    start = 0
      
    for end in range(len(string)):
  
        # Checking if we have already seen the element or not
        if string[end] in seen:
 
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)
  
        # Updating the last seen value of the character
        seen[string[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length



if __name__ == "__main__":
    s = 'geeksforgeeks'
    s = 'aaa'
    s= 'aewergrththy'
    s = 'qwertyuioplkjh'
    print(longest_substr_distinct_char(s))