

# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470706/JavaC%2B%2BPython-Longest-Common-Sequence
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/476662/Python-Clean-DP

# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/


def minInsertions( s):
	n = len(s)
	dp = [[0] * n for _ in range(n)]
	for j in range(n):
		for i in range(j-1,-1,-1):
			dp[i][j] = dp[i+1][j-1] if s[i] == s[j] else min(dp[i+1][j], dp[i][j-1]) + 1
	return dp[0][n-1]



