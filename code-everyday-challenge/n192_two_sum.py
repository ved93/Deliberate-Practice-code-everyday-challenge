

def two_sums(a,target):
    left , right = 0 , len(a)-1

    while left < right:
        sum_ = a[left] + a[right]
        # print(sum_)

        if sum_ > target:
            right -=1
        elif sum_ < target:
            left += 1 
        else:
            return (left, right)

    return -1



from collections import defaultdict

# Returns the indices of two numbers that add up to the target
def two_sums(nums, target):

    lookup = defaultdict(list)
    for i, num in enumerate(nums):
        needed = target - num
        print(i, "  ", num, "  ", lookup)
        if needed in lookup:
            print(lookup[needed])
            return [lookup[needed][0], i]
        lookup[num].append(i)

    return None




if  __name__ == "__main__":
    a = [1,2,7,11,15]
    target = 14
    print(two_sums(a,target))