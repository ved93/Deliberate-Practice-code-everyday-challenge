# Let A[1..n] be an array of integers. For all i from 1 to n find a subarray with maximum sum that
# covers the position i (more formally, for every i, find the largest value A[l] + A[l + 1] + · · · + A[r]
# among all pairs of indices l and r such that 1 ≤ l ≤ i ≤ r ≤ n).
# Input
# The first line contains an integer n (1 ≤ n ≤ 100 000), the number of elements in A.
# The second line contains integers A[1],A[2],...,A[n] (−106 ≤ A[i] ≤ 106).
# Output
# Print n integers separated by spaces. The i-th of them should be equal to the maximal sum of
# subarray among all that cover the position i in A.


#THIS IS WRONG PROGRAM. BELOW IS SOLUTION OF MAX SUM SUB ARRAY PROBLEM

def main(a):
    curr_sum=a[0]
    max_sum=a[0] 

    for i in range(1,len(a)):
        curr_sum=max(curr_sum+a[i],a[i])

        max_sum = max(max_sum, curr_sum)


    return max_sum







if __name__ == "__main__":
    a=[-2,1,-3,4,-1,5,1,-5,4]
    # b, index=naive(a)
    # print(max(b),index[b.index(max(b))])
    # print(b)
    # print(index[27], b[27])

    print(main(a))