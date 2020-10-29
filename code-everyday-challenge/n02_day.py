
#maximum pairwise product
#max product of two distinct numbers in a sequence of non-negative integers


def pairwise_product(nums):
    a= max(nums)
    nums.remove(a)
    b = max(nums)
    return a*b



def pairwise_product_v2(nums):
    max_product =0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            max_product=max(max_product,nums[i]*nums[j])

    return max_product




if __name__ == "__main__":
    # n=int(input())
    # nums=list(map(int, input().split()))
    # print(nums)
    nums= [2, 4, 8, 6]
    print(pairwise_product_v2(nums))






