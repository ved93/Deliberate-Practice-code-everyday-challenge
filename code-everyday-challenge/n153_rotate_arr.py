 

def rotate_array(a,n):
    i = 0
    j = n-1     
    while i != j:
        a[i], a[j] = a[j], a[i]
        i = i + 1
        print(a[j],a)

    return a



if __name__ == "__main__":
    a= [9, 8, 7, 6, 4, 2, 1, 3]
    i = 8
    print(rotate_array(a,i))