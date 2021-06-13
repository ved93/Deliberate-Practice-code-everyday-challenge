



def rearrange(a):
    l,h = 0, len(a)-1

    # for i in range(len(a)):
    while l <= h:

        if a[l] < 0 and a[h] < 0:
            l = l + 1
        elif a[l] > 0 and a[h] < 0:
            tmp = a[l]
            a[l]= a[h]
            a[h] = tmp
            l= l + 1
            h = h+1
        elif a[l] > 0 and a[h] > 0:
            h -= 1

        else:
            l = l + 1
            h -=1

    return a

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print(rearrange(arr))