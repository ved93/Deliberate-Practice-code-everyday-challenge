# https://practice.geeksforgeeks.org/problems/maximum-index-1587115620/1/?track=md-arrays&batchId=144



def max_index(a,n ):
    max_diff = -1

    for i in range(n):

        j = n-1
        while i < j:

            if a[i] <=a[j] and max_diff < (j-i):
                max_diff = j-i

            j = j-1

    return max_diff



# For a given array arr[], 
# returns the maximum j - i
# such that arr[j] > arr[i]
def maxIndexDiff(arr, n):
    maxDiff = 0;
    LMin = [0] * n
    RMax = [0] * n

    # Construct LMin[] such that 
    # LMin[i] stores the minimum 
    # value from (arr[0], arr[1], 
    # ... arr[i]) 
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])

    # Construct RMax[] such that 
    # RMax[j] stores the maximum 
    # value from (arr[j], arr[j + 1],
    # ..arr[n-1]) 
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1]);

    # Traverse both arrays from left
    # to right to find optimum j - i
    # This process is similar to
    # merge() of MergeSort
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1

    return maxDiff




if __name__ == "__main__":
    a = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    print(maxIndexDiff(a, len(a)))