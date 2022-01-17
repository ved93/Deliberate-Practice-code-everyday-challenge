

def merge(left, right):
    d = [None]*(len(left) + len(right))
    i,j,k = 0,0,0
    # print(left, right)

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            d[k] = left[i]
            k +=1
            i += 1
        else:
            d[k] = right[j]
            k +=1
            j += 1
    
    while i < len(left):
        d[k] = left[i]
        i+=1
        k+= 1
    while j < len(right):
        # print(d)
        d[k]=right[j]
        j+=1
        k+=1
    
    # print(d)

    return d





def sort(a):
    n = len(a)
    if n <=1:
        return a

    mid = n//2
    left = sort(a[:mid])
    right = sort(a[mid:])

    d = merge(left, right)

    return d





if __name__ == "__main__":
    a = [5,2,1,6,8,89]
    print(sort(a))