
# https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/

# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/1304346/Simple-Solution-w-Explanation-or-Sliding-Window-Approach-with-Comments

# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/278322/Easy-to-understand-Python-solution

# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/432952/Python-sliding-window-9-lines

# https://leetcode.com/discuss/interview-question/algorithms/125017/amazon-max-consecutive-ones



def longest_ones(nums, k):
    n ,ans, l = len(nums), 0,0
    for r in range(n):

        if nums[r] == 0:
            if k == 0:
                while nums[l]!= 0:
                    l = l + 1
                l = l + 1
            else:
                k = k-1
        
        ans = max(ans, r-l+1)

    return ans





if  __name__ == "__main__":
    a = [1,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1]
    k  =2
    print(longest_ones(a,k))

