

# https://www.geeksforgeeks.org/find-sum-modulo-k-first-n-natural-number/

def find_sum(N,K):
 
    ans = 0
 
    # Counting the number of times
    # 1, 2, .., K-1, 0 sequence occurs.
    y = N / K
 
    # Finding the number of elements
    # left which are incomplete of
    # sequence Leads to Case 1 type.
    x = N % K
 
    # adding multiplication of number
    # of times 1, 2, .., K-1, 0
    # sequence occurs and sum of
    # first k natural number and
    # sequence from case 1.
    ans = ((K * (K - 1) / 2) * y +
                (x * (x + 1)) / 2)
 
    return int(ans)
 


if __name__ == "__main__":
    N = 10
    K = 2
    print(find_sum(N, K))