

def binary_search(a,k):
    left, right = 0, len(a)-1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == k:
            return True
        
        elif a[mid] < k:
            left = mid +1
        else:
            right = mid - 1

    return -1







if __name__ == "__main__":
    a = [1,3, 4,5, 8,9,10]
    k = 10
    print(binary_search(a,k))