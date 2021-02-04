
#https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/


def findPivot(arr, low, high): 
      
    # base cases 
    if high < low: 
        return -1
    if high == low: 
        return low 
      
    # low + (high - low)/2; 
    mid = int((low + high)/2) 
    # print(mid,low)
      
    if mid < high and arr[mid] > arr[mid + 1]: 
        # print('dont')
        return mid 
    if mid > low and arr[mid] < arr[mid - 1]: 
        # print('hw')
        return (mid-1) 
    if arr[low] >= arr[mid]:
        # print('dont truse') 
        return findPivot(arr, low, mid-1) 
    return findPivot(arr, mid + 1, high) 




# print(findPivot([3, 4, 5, 6, 7,1, 2],0,6))
# print(findPivot([ 6, 7,1, 2,3,4,5],0,6))

def binary_search(arr,left,right,key):
    mid = (left+ right)//2

    while left <= right:
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr,mid+1,right, key)
        else:
            return binary_search(arr,left,mid-1,key)




def pivotedBinarySearch(arr, n, key):
    pivot = findPivot(arr, 0,n-1)

    if pivot == -1:
        return binary_search(arr, 0, n-1, key)

    if arr[pivot] == key:
        return pivot
    if arr[0]<= key:
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr,pivot+1,n-1, key) 




# Let us search 3 in below array 
arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
n = len(arr1) 
key = 3
print("Index of the element is : ",  
      pivotedBinarySearch(arr1, n, key)) 