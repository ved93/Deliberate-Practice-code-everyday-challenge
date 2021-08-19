




def binary_search(a,k, low, high):
    mid = (low+high)//2

    if len(a[low:high+1]) <=1:
        # print(a[low:high+1], a[0])
        if a[mid] == k:
            return mid
        else:
            return -1


    if a[mid] == k:
        return mid
    elif a[mid] >= k:
        return binary_search(a,k,low, mid)
    elif a[mid] < k:
        return binary_search(a,k, mid+1,high)
    else:
        return -1



def binary_search_v2(a,k):
    low, high = 0, len(a)-1

    while low <= high:
        mid  = (low+high)//2

        if a[mid] == k:
            return mid
        elif a[mid] >= k:
            high = mid
        else:
            low = mid+1
    return -1










if __name__ == "__main__":
    a = [0, 2, 3, 4, 5, 6, 7, 8, 9, 18]
    # a = sorted(a)
    # print(a)
    # print(binary_search(a,72, 0, len(a)-1))
    print(binary_search_v2(a,18))
