


# https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP

# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).

def longestPalindrome( s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            if i ==0:
                longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) <= len(s[i:j+1]):
                            # print("Maximum palindrom   ", longest_palindrom)
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom


def longestPalSubstr(st) :
    n = len(st) # get length of input string
 
    # table[i][j] will be false if substring
    # str[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y
                          in range(n)]
     
    # All substrings of length 1 are
    # palindromes
    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1
     
    # check for sub-string of length 2.
    start = 0
    i = 0
    while i < n - 1 :
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1
     
    # Check for lengths greater than 2.
    # k is length of substring
    k = 3
    while k <= n :
        # Fix the starting index
        i = 0
        while i < (n - k + 1) :
             
            # Get the ending index of
            # substring from starting
            # index i and length k
            j = i + k - 1
     
            # checking for sub-string from
            # ith index to jth index iff
            # st[i + 1] to st[(j-1)] is a
            # palindrome
            if (table[i + 1][j - 1] and
                      st[i] == st[j]) :
                table[i][j] = True
     
                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1
    # print "Longest palindrome substring is: ", printSubStr(st, start,
                                            #    start + maxLength - 1)
 
    # return maxLength # return length of LPS
    return st[start:start + maxLength]





if __name__ == "__main__":

    s = "kjqlrzzfmlvyoshiktodnsjjp"
    # print(longestPalSubstr(s))
    print(longestPalindrome(s))
