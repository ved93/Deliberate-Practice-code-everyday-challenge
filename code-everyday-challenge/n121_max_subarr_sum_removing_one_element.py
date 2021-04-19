

# https://www.geeksforgeeks.org/maximum-sum-subarray-removing-one-element/amp/?ref=rp

def maxSumSubarrayRemovingOneEle(arr,n):
    fw  = [0 for k in range(n)]
    bw = [0 for k in range(n)]

    curr_max= max_so_far = arr[0]

    fw[0] = curr_max

    for i in range(1,n):
        curr_max = max(arr[i], curr_max+arr[i])

        max_so_far = max(max_so_far, curr_max)

        fw[i] = curr_max


    curr_max = max_so_far = bw[n-1] = arr[n-1]
    i = n-2

    while i >= 0:
        curr_max =max(arr[i], curr_max+arr[i])
        max_so_far = max(curr_max, max_so_far)

        bw[i]= curr_max
        i -= 1

        #  Initializing final ans by max_so_far so that,

    #  case when no element is removed to get max sum

    #  subarray is also handled

    fans = max_so_far

    for i in range(1,n-1):

        fans = max(fans, fw[i - 1] + bw[i + 1])

  

    return fans









if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]

    n = len(arr)

    print(maxSumSubarrayRemovingOneEle(arr, n))
