



class pair():
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(a, n):
    minmax = pair()

    if n ==1:
        minmax.min = a[0]
        minmax.max = a[0]

        return minmax
    
    if a[0]>a[1]:
        minmax.max = a[0]
        minmax.min = a[1]
    else:
        minmax.min = a[0]
        minmax.max = a[1]


    for i in range(2, n):
        
        if a[i]> minmax.max:
            minmax.max = a[i]
        elif a[i]< minmax.min:
            minmax.min = a[i]

    return minmax



def getMinMax_re(l,h,a):

    if l == h:
        return a[0],a[0]
    
    #if two ele
    elif l+1 == h:
        if a[l] > a[h]:
            arr_max = a[l]
            arr_min = a[h]
        else:
            arr_max = a[h]
            arr_min = a[l]
        return arr_max,arr_min

    else:
        #if more than 2 elements

        mid = (l+h)//2

        arr_max1,arr_min1=getMinMax_re(l,mid,a) 
        arr_max2,arr_min2 = getMinMax_re(mid+1,h,a)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))








if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

    high = len(arr) - 1
    low = 0
    arr_max, arr_min = getMinMax_re(low, high, arr)
    print('Minimum element is ', arr_min)
    print('nMaximum element is ', arr_max)
