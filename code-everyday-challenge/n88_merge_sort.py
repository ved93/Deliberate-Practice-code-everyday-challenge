

def merge(left, right):
    i,j,k = 0,0,0
    d = []#[0]*(len(left) + len(right))

    print(left, right)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # d[k] =left[i]
            d.append(left[i])
            k = k+1
            i = i+1
        else:
            # d[k] = right[j]
            d.append(right[j])
            k = k+1
            j = j+1
        
    if i < len(left):
        d.extend(left[i:])
    if j < len(right):
        d.extend(right[j:])

    return d


def merge_sort(a):
    n = len(a)
    mid = n//2

    if n <= 1:
        return a

    # print(a[:mid],'   ',a[mid:])
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    # print(left, right)
    d=merge(left, right)

    return d





if __name__ == "__main__":

    a=[12, 11, 13, 5, 6, 7]
    print(merge_sort(a)) 


