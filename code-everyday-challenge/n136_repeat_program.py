

def merge(left, right):
    a= [] #[None]*(len(left)+len(right))
    i=j=k =0

    while i <= len(left)-1 and j <= len(right)-1:  
        if left[i] <= right[j]:
            # a[k] = left[i]
            a.append(left[i])    
            k += 1
            i += 1
        else :
            # a[k] = right[j]
            a.append(right[j])
            k += 1
            j += 1

        # print(i, j, left, right)

    if i <= len(left):
        a.extend(left[i:])

    if j <= len(right):
        a.extend(right[j:])

    return a


def merge_sort(a):
    if len(a) <= 1:
        return a

    l, r = 0,len(a)-1


    mid = (l+r)//2
    left=merge_sort(a[:mid+1])
    right = merge_sort(a[mid+1:])

    d=merge(left,right)


    return d









if __name__ == "__main__":
    a= [7, 2, 1, 3, 8, 4, 9, 1, 2, 6]
    print(merge_sort(a))