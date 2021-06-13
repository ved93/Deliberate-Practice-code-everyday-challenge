def merge(left, right):
    a=[None]*(len(left)+ len(right))
    i,j,k = 0,0,0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            a[k] = left[i]
            k = k+1
            i= i+1
        else:
            a[k] = right[j]
            k= k+1
            j = j+1


    if i < len(left):

        while i < len(left):
            a[k] = left[i]
            i = i+1
            k = k+1

    if j < len(right):
        while j < len(right):
            a[k] = right[j]
            j = j+1
            k = k+1

    return a


def merge_sort(a ):
    mid = (len(a)) //2

    if len(a) <= 1:
        return a

    left=merge_sort(a[:mid])

    right = merge_sort(a[mid:])

    d = merge(left,right)

    return d



if __name__ =='__main__':
    a= [7, 2, 1, 3, 8, 4, 9, 1, 2, 6]


    print(merge_sort(a))