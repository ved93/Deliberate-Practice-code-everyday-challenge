

def merge(left, right):
    m = []

    i,j = 0,0 
    k = 0

    while i < len(left) and j < len(right):
        # print(left,right,left[i], right[j])
        if left[i] <= right[j]:
            m.append(left[i])

            i+=1
        else:
            m.append(right[j])
            j +=1

    
    if i < len(left):
        m.extend(left[i:])
    
    if j < len(right):
        m.extend(right[j:])

    print(left, right)
    print(m)
    return m




def sort(a):
    n  = len(a)
    mid = n//2

    if n <= 1:
        return a

    left = sort(a[:mid])
    right = sort(a[mid:])

    m=merge(left, right)

    return m





if __name__ == "__main__":
    a= [5,1,5,8,12,13,5,8,1,23,1,11]
    print(sort(a))