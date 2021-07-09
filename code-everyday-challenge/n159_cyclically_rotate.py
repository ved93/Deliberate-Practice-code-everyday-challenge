
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1

# Given an array, rotate the array by one position in clock-wise direction.

# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4
def rotate_cycle(a):
    n = len(a)
    tmp = a[-1] 
    for i in range(1,n):
        a[-i] = a[-i-1]

    a[0] = tmp    
    return a




if __name__ == "__main__":
    a = [1, 2, 3,4,5]
    print(rotate_cycle(a))