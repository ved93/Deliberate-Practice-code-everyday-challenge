

# https://leetcode.com/problems/max-consecutive-ones/


def count_consecutive_ones(a):
    max_so_far = 0

    if not a: return 0
    k = 0
    for i in range(len(a)):

        if a[i] == 1:
            k = k + 1
        else:
            max_so_far = max(max_so_far, k)
            k = 0
        
    max_so_far = max(max_so_far, k)

    return max_so_far
    








if __name__ == "__main__":
    a = [1,1,0,1,1,1]
    a = [1,0,1,1,0,1]
    print(count_consecutive_ones(a))