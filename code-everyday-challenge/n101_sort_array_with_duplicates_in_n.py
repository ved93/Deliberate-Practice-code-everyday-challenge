# 
# Efficiently sort an array with many duplicated values with given range
# Input:  { 4, 2, 40, 10, 10, 1, 4, 2, 1, 10, 40 }
# Output: { 1, 1, 2, 2, 4, 4, 10, 10, 10, 40, 40 }

#complexity o(n+k) n- input size and k is input range

RANGE = 100
 
# Function to efficiently sort a list with many duplicated values
# using the counting sort algorithm
def customSort(A):
 
    # create a new list to store counts of elements in the input list
    freq = [0] * RANGE
 
    # using the value of elements in the input list as an index,
    # update their frequencies in the new list
    for i in A:
        freq[i] = freq[i] + 1
 
    # overwrite the input list with sorted order
    k = 0
    for i in range(RANGE):
        while freq[i] > 0:
            A[k] = i
            freq[i] = freq[i] - 1
            k = k + 1



if __name__ == '__main__':
 
    A = [4, 2, 40, 10, 10, 1, 4, 2, 1, 10, 40]
 
    customSort(A)
    print(A)

