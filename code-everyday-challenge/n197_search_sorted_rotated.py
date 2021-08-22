
#n99_search_rotated file
# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/?ref=leftbar-rightbar



def binary_search(a,k, low, high):
    mid = (low+high)//2

    if low <= high:

        if a[mid ] == k:
            return mid
        elif a[mid] > k: 
            return binary_search(a,k,low, mid )
        else:
            return binary_search(a, k, mid+1, high)
    else:
        return -1



def search_rotated_array(a,k):
    low, high = 0, len(a)-1

    mid = (low+high)//2

    if (a[mid] >= k and a[low] <= k) or  (a[mid] <= k and a[high] <= k):
        return binary_search(a,k, low, mid)

    elif (a[mid] > k and a[low] > k) or  (a[mid] < k and a[high] > k):
        return binary_search(a,k, mid+1, high)

    return -1




if __name__ == "__main__":
    a = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    # a = sorted(a)
    # print(a)
    # print(binary_search(a,72, 0, len(a)-1))
    print(search_rotated_array(a,9))