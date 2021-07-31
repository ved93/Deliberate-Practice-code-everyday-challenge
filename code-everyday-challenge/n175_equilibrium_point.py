


def equilibriumPoint(A, N):
    # Your code here
    if N <= 1:
        return 1
    
    left, right = A[0],sum(A[2:])
    for i in range(1,N-1):        
        # if sum(A[:i]) == sum(A[i+1:]):
        #     return i+1
        if left  == right:
            return i+1
        else:
            left = left + A[i]
            right = right - A[i+1]


            
    return -1


a = [1,3,5,2,2]
n = 5
print(equilibriumPoint(a,n))