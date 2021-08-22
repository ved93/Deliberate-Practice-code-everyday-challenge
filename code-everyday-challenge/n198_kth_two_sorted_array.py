


def get_kth_element(a,b,k):

    c = [None]*(len(a)+len(b))
    m = 0
    i,j =0,0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            c[m] = a[i]
            i = i +1
        else:
            c[m] = b[j]
            j = j+1
        m = m+1

    while i < len(a):
        c[m] = a[i]
        m = m+1
        i = i+1
    while j < len(b):
        c[m] = b[j]
        m = m+1
        j = j+1

    return c[k-1]



if __name__ == "__main__":
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5

    print(get_kth_element(a, b,k))