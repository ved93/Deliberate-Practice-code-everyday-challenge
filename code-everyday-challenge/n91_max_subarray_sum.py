# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

def naive(a):
    store = []
    index = []
    for i in range(len(a)):

        for j in range(i+1, len(a)):

            store.append(sum(a[i:j+1]))
            index.append([i,j])

    return store,index


def maxSubArray( nums ) :
    n = len(nums)
    curr_sum = max_sum = nums[0]

    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        print(nums[i],'  ',curr_sum, '  ',max_sum)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum


a=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# store,index=naive(a)
# l,r=index[store.index(max(store))][0],index[store.index(max(store))][1]
# print(sum(a[l:r+1]),a[l:r+1] )
