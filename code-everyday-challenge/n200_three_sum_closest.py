# https://leetcode.com/problems/3sum-closest/discuss/8026/Python-solution-(two-pointer).
# https://leetcode.com/problems/3sum-closest/discuss/778177/Python3-%3A-Runtime%3A-52-ms-faster-than-99.77

# https://www.geeksforgeeks.org/find-a-triplet-in-an-array-whose-sum-is-closest-to-a-given-number/

def three_sum_closest(a,target):
    a = sorted(a)
    if len(a) < 3:
        return -1

    result = a[0]+a[1]+a[2]

    prev, next = 0,0

    for i in range(len(a)-2):

        left , right = i+1, len(a)-1

        while left < right:
            curSum = a[i]+a[left] + a[right]

            if curSum == target:
                return curSum
            
            if abs(curSum-target) < abs(result -target):
                result = curSum

            if curSum < target:
                prev = curSum
                left=left+1
            elif curSum > target:
                next = curSum
                right-=1

        # if abs(prev-target) ==abs(next-target):
        result = max(prev, next)

    return result 





if  __name__ == "__main__":
    a = [5,2,7,5]
    target = 13
    print(three_sum_closest(a, target))



























































































































































