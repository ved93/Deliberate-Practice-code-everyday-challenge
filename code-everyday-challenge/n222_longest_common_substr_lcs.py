
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/768495/longest-common-substring-python-dp-solution

# https://leetcode.com/problems/longest-common-subsequence/discuss/598508/Python-DP-solution-with-Explanation-%2B-Thinking-process-%2B-Diagram

# https://leetcode.com/problems/longest-common-subsequence/discuss/598285/Python-faster-than-90

class Solution:
	def findLength(self, A , B) -> int:

		n = len(A)
		m = len(B)
		
		#Edge cases.
		if m == 0 or n == 0:
			return 0

		if n == 1 and m == 1:
			if A[0] == B[0]:
				return 1
			else:
				return 0
		
		#Initializing first row and column with 0 (for ease i intialized everthing 0 :p)
		dp = [[0 for x in range(m + 1)] for y in range(n + 1)]

		final = 0
		
		#this code is a lot like longest common subsequence(only else condition is different). 
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if A[i - 1] == B[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]

				else:
					dp[i][j] = 0

				final = max(final, dp[i][j])

		return final