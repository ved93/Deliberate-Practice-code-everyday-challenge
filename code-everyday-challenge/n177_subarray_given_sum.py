
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1/?track=md-arrays&batchId=144

def sub_arr_sum(arr, n, sum_):
    #Write your code here
    curr_sum = arr[0]
    start = 0


    i =1
    while i<= n:

        while curr_sum > sum_ and start < i-1:
            curr_sum -= arr[start]
            start += 1

        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum_:
            # print ("Sum found between indexes")
            # print ("% d and % d"%(start, i-1))
            return [start+1, i]
    
        # Add this element
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1
    
    # If we reach here,
    # then no subarray
    # print ("No subarray found")
    return [-1]
 
# Driver program
arr = [1,2, 3, 7, 5]  #[15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 12 #23
 
print(sub_arr_sum(arr, n, sum_))