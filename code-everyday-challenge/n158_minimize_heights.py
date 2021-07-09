
#https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
# https://leetcode.com/problems/smallest-range-ii/discuss/980552/Python-O(NlogN)-Time-easy-to-understand
# https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/


def minimize_heights(a,k,n):

    if n <= 1:
        return 0

    a = sorted(a)
    diff = a[n-1]-a[0]

    minimum = a[0]+k
    maximum = a[n-1]-k

    if minimum > maximum:
        minimum,maximum = maximum, minimum

    for i in range(n):
        sub = a[i]-k 
        add = a[i]+k

        if (sub >= minimum) or (add <= maximum):
            continue

        if (maximum-sub) <= (add-minimum):
            minimum = sub

        else:
            maximum = add

    
    return min(diff, maximum-minimum)



def smallestRangeII(A,K,n):
    A.sort()
    res = A[-1] - A[0]  # possible result

    for i in range(len(A) - 1):
        a, b = A[i], A[i+1]
        hi = max(A[-1] - K, a + K)  # possible max num
        lo = min(A[0] + K, b - K)  # possible min num
        res = min(res, hi - lo)

    return res





if __name__ == "__main__":
    a = [1,5,15,10]
    k= 3
    N= 4
    print(minimize_heights(a,k,N))
    print(smallestRangeII(a,k,N))
