
#https://www.geeksforgeeks.org/python-program-for-binary-search/

def binary_search(a,low, high,value):
    
    if high>= low:
        mid = (low+high)//2

        if a[mid] < value:
            return binary_search(a,mid+1,high,value)
        elif a[mid] > value:
            return binary_search(a,low,mid-1,value)
        else:
            return mid
    else:
        # print(low, high)
        return -1




test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list,0,len(test_list)-1, test_val2))
print(binary_search(test_list,0,len(test_list)-1, 30))