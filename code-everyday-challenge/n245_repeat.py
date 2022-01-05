
def merge(left, right):
    m = [None]*len(left) + [None]*len(right)
    i,j,k = 0,0,0
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            m[k] = left[i]
            i = i+1
        else:
            m[k] = right[j]
            j = j+1

        k = k+1


    while i < len(left):
        m[k] = left[i]
        i +=1
        k +=1
    
    while j < len(right):
        m[k] = right[j]
        k +=1
        j +=1
    
    return m





def merge_sort(a):

    if len(a) <=1:
        return a
    
    mid = len(a) // 2

    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    merged = merge(left, right)

    return merged 



if __name__ == '__main__':
    # n = int(input())
    # for i in range(0, n):
    #     print(i * i)
    import random

    random.seed(1)
    # n=random.randint(1, 10)
    n = 10
    l = random.sample(range(1, 50), n)
    # print(l)

    print(merge_sort(l))