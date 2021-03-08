
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def naive(a):
    b = []
    index = []
    for i in range(len(a)):

        for j in range(i,len(a)):
            b.append(sum(a[i:j+1]))
            index.append([i,j])


    return b, index


def main(a):
    curr_sum = max_sum = a[0]

    for i in range(1,len(a)):
        curr_sum=max(a[i], curr_sum+a[i])

        max_sum = max(max_sum, curr_sum)


    return max_sum






if __name__ == "__main__":
    a=[-2,1,-3,4,-1,5,1,-5,4]
    # b, index=naive(a)
    # print(max(b),index[b.index(max(b))])
    # print(b)
    # print(index[27], b[27])

    print(main(a))
    
