

def binary_search(a,x):

    left, right = 0, len(a)-1


    while left <= right:

        mid = (left + right) // 2
        if a[mid]== x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1



if __name__ == "__main__":
    a= [10,16,4,8,17]
    a= sorted(a)
    print(a)
    x= 17
    print(binary_search(a,x))