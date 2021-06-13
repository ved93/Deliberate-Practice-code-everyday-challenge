
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(a):
    max_sum = 0

    max_so_far = 0

    for i in range(len(a)):
        max_sum = max(a[i], max_sum+a[i])

        max_so_far = max(max_so_far, max_sum)


    return max_so_far






print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))