
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

def longest_substring(s):
    prevChar = ""
    currentString = ""
    longestString = ""

    for char in s:
        if prevChar <= char:
            currentString += char
            if len(currentString) > len(longestString):
                longestString = currentString
        else:
            currentString = char
        prevChar = char
    print('Longest substring in alphabetical order is: ' + longestString )

    return longestString



if __name__ == "__main__":
    s= 'azcbobobegghakl'
    print(longest_substring(s))