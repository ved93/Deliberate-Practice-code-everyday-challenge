# https://practice.geeksforgeeks.org/problems/trailing-zeroes-in-factorial5134/1/?track=MD-Math&batchId=144

#https://leetcode.com/problems/factorial-trailing-zeroes/discuss/522315/Clear-explanation-of-the-solution-since-I-didn't-find-an-adequate-one


def trailingZeroes( N):
    #code here 
    cnt = 0
    while N!=0:
        N = N//5
        cnt =cnt+N
    return cnt


print(trailingZeroes(100))