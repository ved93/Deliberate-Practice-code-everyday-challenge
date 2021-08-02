
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1/?track=md-arrays&batchId=144#
# https://www.geeksforgeeks.org/leaders-in-an-array/

def leaders(A,N):
        #Code here
            
    ls = []
    max_from_right = A[-1]
    for i in range(N-2,-1,-1):
        
        # max_ele=max(A[i+1:])
        # print(A[i])
        if max_from_right <= A[i]:
            # max_ele=max(A[i+1:])
            ls.append(A[i])
            max_from_right = A[i]

    ls=ls[::-1]
    ls.append(A[-1])

    return ls

a= [16,17,4,3,5,2]
n = 6

print(leaders(a,n))
