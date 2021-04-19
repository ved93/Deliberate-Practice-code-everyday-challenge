
# Problem 1
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

def count_vowel(s):
    count = 0
    for chr in s:
        if chr in [ 'a', 'e', 'i', 'o','u']:
            count += 1

    return count



if __name__ == "__main__":
    s= 'azcbobobegghakl'
    print(count_vowel(s))