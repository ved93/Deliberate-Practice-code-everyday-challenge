
# https://www.geeksforgeeks.org/how-to-sort-an-array-in-a-single-loop/


def sort_array(a):
    length=len(a)

    j = 0
    while j < length-1:

        if (a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

            # updating the value of j = -1
            # so after getting updated for j++
            # in the loop it becomes 0 and
            # the loop begins from the start.

            j= -1

        j+=1

    return a



if __name__ == "__main__":
    # Declaring an integer array of size 11.
    arr = [1, 2, 99, 9, 8, 
           7, 6, 0, 5, 4, 3]
  
    # Printing the original Array.
    print("Original array: ", arr)
  
    # Sorting the array using a single loop
    arr = sort_array(arr)
  
    # Printing the sorted array.
    print("Sorted array: ", arr)