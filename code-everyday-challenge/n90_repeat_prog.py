

def merge(left, right):
    i,j,k = 0,0,0
    d = [None]*(len(left) + len(right))

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            d[k] = left[i]
            i +=1
            k+=1 
        else:
            d[k] = right[j]
            j+=1
            k+=1

    while i < len(left):
        d[k] = left[i]
        i+=1
        k+=1

    while j < len(right):
        d[k] = right[j]
        j+=1
        k+=1

    return d



def merge_sort(a):

    if len(a) <= 1:
        return a

    mid = len(a) //2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    d=merge(left, right)

    return d


if __name__ == "__main__":
    a=[12, 11, 13, 5, 6, 7]
    print(merge_sort(a)) 

