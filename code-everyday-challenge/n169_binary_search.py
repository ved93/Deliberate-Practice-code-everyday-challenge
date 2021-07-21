def binary_search(input_array, value):
    """Your code goes here."""
    # mid  = len(input_array)//2
    # if input_array[mid] < value:
    #     return binary_search(input_array[mid+1:],value)
    # elif input_array[mid] > value:
    #     return binary_search(input_array[:mid],value)
    # elif input_array[mid] == value:
    #     # print('rfr', mid)
    #     return input_array.index(value)
    # else:
    #     return -1

    low = 0 
    high = len(input_array)



    while (low <= high):
        mid = (low+high)//2

        if input_array[mid] < value:
            low = mid+1
            # continue 
        elif input_array[mid] > value:
            # mid = (len(input_array[:mid]))//2
            high = mid-1
            # continue 
        elif input_array[mid] == value:
            return input_array.index(value)

    # if mid < 0 or mid > len(input_array):
    #     return -1
    # return input_array.index(value)    
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val1))
