# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# calc max sum
def max_sum_subarr(a):
    n = len(a)
    index = []
    curr_sum = max_sum = a[0]

    for i in range(n):
        curr_sum = max(a[i], curr_sum+a[i])

        max_sum = max(max_sum, curr_sum)


    return max_sum



if __name__ == "__main__":
    a = [-2,1,-3,4,-1,2,1,-5,4]

    print(max_sum_subarr(a))