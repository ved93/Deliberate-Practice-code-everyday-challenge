
def merge(b,c):
    i,j,k=0,0,0
    d=(len(c)+len(b))*[0]
    while i < len(b) and j < len(c): 
        if b[i] <= c[j]:
            d[k] = b[i]
            i = i+1
        else:
            d[k] = c[j]
            j = j+1
        
        k = k+1

    while i < len(b) :
        d[k] = b[i]
        i = i+1
        k = k+1
    while j < len(c) : 
        d[k] = c[j]
        j = j+1
        k = k+1
    return d








def merge_sort(a):
    if len(a) <= 1:
        return a

    n = len(a)
    mid = n//2
    left = a[:mid]
    right = a[mid:]
    b = merge_sort(left)
    c = merge_sort(right)
    # print(b, ''  ,c)
    # print(left,'' ,right)
    d = merge(b,c)
    return d



if __name__ == "__main__":

    a=[12, 11, 13, 5, 6, 7]
    print(merge_sort(a)) 








