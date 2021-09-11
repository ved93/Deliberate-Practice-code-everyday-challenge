
# https://leetcode.com/problems/break-a-palindrome/

# Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

# Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



# https://leetcode.com/problems/break-a-palindrome/discuss/907823/Very-simple-python-solution-O(N)-time-and-space

# https://leetcode.com/problems/break-a-palindrome/discuss/892711/Python-Solution.-Readable.-simple-code.#

# https://leetcode.com/problems/break-a-palindrome/discuss/1364895/python-or-better-than-95-orsimple



# Explanation
# If length of palindrome == 1, return ''
# For even length string, if we found a char that is not a, replace it with a and return
# For odd length string, if we find a char that is not a and it's not the middle of string, replace it with a and return
# If all a in the string, replace the last char to b

# https://leetcode.com/problems/break-a-palindrome/discuss/846873/Python-3-or-Greedy-one-pass-or-Explanations



def breakPalindrome( palindrome: str) -> str:
    n=len(palindrome)
    if n==1:
        return ""
    if n%2==0:
        for j,i in enumerate(palindrome):
            if i!="a":
                return palindrome[:j]+"a"+palindrome[j+1:]
        return palindrome[:-1]+"b"
    
    else:
        for j,i in enumerate(palindrome):
            if j!=n//2 and i!="a":
                return palindrome[:j]+"a"+palindrome[j+1:]
        return palindrome[:-1]+"b"