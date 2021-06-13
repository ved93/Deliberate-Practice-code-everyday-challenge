

def sort_arr(a):
    cnt_0, cnt_1, cnt_2 = 0,0,0
    
    for i in a:
        
        if i == 0:
            cnt_0 += 1
        if i == 1:
            cnt_1 += 1
        if i == 2:
            cnt_2 += 1
        
    i = 0
    while cnt_0 > 0:
        a[i] = 0

        i = i+1
        cnt_0 -= 1

    while cnt_1 > 0:
        a[i] = 1

        i = i+1
        cnt_1 -= 1

    while cnt_2 > 0:
        a[i] = 2

        i = i+1
        cnt_2 -= 1

    
    return a





def sort_pointers(a):
    l,mid = 0,0
    h = len(a)-1

    while mid <= h:

        if a[mid] ==0:
            a[l], a[mid]= a[mid], a[l]
            mid += 1
            l += 1
        if a[mid] == 1:
            mid += 1
        if a[mid] == 2:
            a[h],a[mid]= a[mid], a[h]
            mid += 1
            h -= 1

        
    return a








if __name__ == "__main__":
    a = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

    print(sort_arr(a))
    print(sort_pointers(a))