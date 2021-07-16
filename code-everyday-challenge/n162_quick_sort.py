
# https://www.programiz.com/dsa/quick-sort

# https://www.geeksforgeeks.org/quick-sort/

#https://www.educative.io/edpresso/how-to-implement-quicksort-in-python

def partition(a,low, high):
    pivot = a[high]
    i = low-1

    for j in range(low,high):

        if a[j] <= pivot:
            i = i+1

            a[i],a[j] = a[j],a[i]

    a[i+1],a[high] = a[high],a[i+1]

    return i+1


def quick_sort(a,low, high):
    if low < high:
        pi = partition(a, low, high)

        quick_sort(a,low,pi-1)

        quick_sort(a,pi+1,high)

    return a






if __name__ == "__main__":
    data = [8, 7, 2, 1, 0, 9, 6]

    print(quick_sort(data, 0,len(data)-1))

