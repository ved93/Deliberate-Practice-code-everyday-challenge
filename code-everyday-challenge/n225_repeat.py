


def binary_search(a,k):
    l ,r = 0 , len(a)-1
    # prev = float(inf)

    # print(prev)

    while l < r:
        mid = (l+r)//2

        if a[mid] < k:
            l= mid+1
        elif a[mid] > k:
            r= mid-1
        else:
            return mid

    return -1












if __name__ == "__main__":
    a= [5,1,5,8,12,13,5,8,1,23,1,11]
    k = 5
    a = sorted(a)
    a = [1, 1, 1, 5, 5, 5, 8, 8, 11, 12, 13, 23]

    print(binary_search(a, k))