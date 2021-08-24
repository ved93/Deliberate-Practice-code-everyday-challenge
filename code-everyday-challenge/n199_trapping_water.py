
# https://www.geeksforgeeks.org/trapping-rain-water/





# def trapping_water(a):
#     left, right = 0, len(a)-1
#     min_bar = min(a[left], a[right])

#     if min_bar == min(a):
#         a.remove(min_bar)
#         # left, right = 0, len(a)-1
#         print(a)
#         # min_bar = min(a[left], a[right])

#         return trapping_water(a)

#     left = left + 1
#     total = 0
#     while left < right:

#         if a[left] < min_bar:
#             total = total + (min_bar-a[left])
#         left = left+1
#     return total


def findWater(arr, n):
 
    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n
 
    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n
 
    # Initialize result
    water = 0
 
    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])
 
    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);
 
    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]
 
    return water


def maxWater(arr, n):
    # indices to traverse the array
    left = 0
    right = n-1
 
    # To store Left max and right max
    # for two pointers left and right
    l_max = 0
    r_max = 0
 
    # To store the total amount
    # of rain water trapped
    result = 0
    while (left <= right):
         
        # We need check for minimum of left
        # and right max for each element
        if r_max <= l_max:
             
            # Add the difference between
            #current value and right max at index r
            result += max(0, r_max-arr[right])
             
            # Update right max
            r_max = max(r_max, arr[right])
             
            # Update right pointer
            right -= 1
        else:
             
            # Add the difference between
            # current value and left max at index l
            result += max(0, l_max-arr[left])
             
            # Update left max
            l_max = max(l_max, arr[left])
             
            # Update left pointer
            left += 1
    return result



if __name__ == "__main__":
    a = [3,0,0,2,0,4]
    a = [7,4,0,9]
    a = [6,9,9]
    a = [8, 8, 2, 4, 5, 5, 1]
    a = [1, 1, 5, 2, 7, 6, 1, 4, 2, 3]
    # a.remove(1)
    # print(a)
    print(maxWater(a, len(a)))