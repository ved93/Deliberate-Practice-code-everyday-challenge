

# https://leetcode.com/problems/longest-happy-prefix/discuss/547187/Python-Deterministic-Finite-Automaton-inspired-by-KMP

# https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1/?track=md-string&batchId=144#

# Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.
# Input: s = "abab"
# Output: 2
# Explanation: "ab" is the longest proper 
# prefix and suffix. 


def lps(s):
    from collections import Counter
    if len(Counter(s)) == 1: return len(s)-1

    # if 

    prefix = ''

    for i,char in enumerate(s):

        if char == s[-1] and s[0] ==s[-i-1] and i <= len(s)-i-1:
            prefix = s[:i+1]
            # print(prefix,i ,'here', char,s[-1] ,' ',s[0] ,s[-i-1])

            # break

    
    return len(prefix)

def longestPrefix( s: str) -> str:
    i = len(s)-1
    while i > 0:
        if s[:i] == s[-i:]:
            return len(s[:i])
        i -= 1
    return 0
        









if __name__ == "__main__":
    s = 'ababdede'
    s= 'sspss'
    s=  'ababababababab'
    # print(lps(s))
    print(longestPrefix(s))