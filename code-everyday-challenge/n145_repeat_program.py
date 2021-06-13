

def find_lis(a):
    T = [None]*len(a)
    prev = [None]*len(a)

    for i in range(len(a)):
        T[i] = 1
        prev[i] = -1

        for j in range(i):

            if a[j] <= a[i] and T[i]< T[j]+1:

                T[i] = T[j]+1

                prev[i] = j

    longest =max(T)
    i = 0

    for i in range( len(a)):
        if T[i] == longest:
   
            break
    
    store = []
    while i > 0:

        store.append(a[i])

        i = prev[i]


    return store





if __name__ =='__main__':
    a= [7, 2, 1, 3, 8, 4, 9, 1, 2, 6]
    # a= [1, 7,2, 3, 8, 4, 9 ]


    print(find_lis(a))