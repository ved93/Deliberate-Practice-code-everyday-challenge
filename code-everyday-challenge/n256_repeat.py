

def binary_search(a,k):
    l,r = 0 , len(a)-1
    while l <= r:
        mid = (l+r)//2
        if a[mid] == k:
            return mid
        elif a[mid] > k:
            r = mid-1
        else:
            l = mid+1
    
    return -1


def binary_search_v2(a,k):
    n = len(a)
    if n == 0:
        return -1
    # if n == 1:
    #     return 0 if a[0] == k else -1

    mid = n//2
    
    if a[mid] == k:
        return mid
    elif a[mid] > k:
        return binary_search_v2(a[:mid],k)
    else:
        return binary_search_v2(a[mid:],k) + mid


def binary_search_v3(a,k,l,h):
    # low, high = 0, len(a)-1
    if l > h:
        return -1
    mid = (l+h)//2
    if a[mid] == k:
        return mid
    elif a[mid] > k:
        return binary_search_v3(a,k,l,mid-1)
    else:
        return binary_search_v3(a,k,mid+1,h)
    






if __name__ == "__main__":
    a = [5,2,1,6,8,89]
    k = 8
    a = sorted(a)
    print(a)
    print(binary_search_v2(a,k))
    print(binary_search_v3(a,k, 0, len(a)))
