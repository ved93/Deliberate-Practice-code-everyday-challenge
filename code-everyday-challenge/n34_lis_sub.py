

def lis( A):
    T= [None]*len( A)
    prev = [None]*len( A)

    for i in range(len( A)):
        T[i] = 1
        prev[i] = -1 

        for j in range(i):
            if A[j] < A[i] and T[i] < T[j]+1:
                T[i] = T[j]+1
                prev[j] = i

    longest =max(T)

    for i in range( len(A)):
        if A[i] == longest:
   
            break
    last_index = i

    store = []
    while last_index > 0 :
        store.append(last_index)

        last_index = prev[last_index]

    print(prev)
    store.reverse()

    return store






if __name__ == "__main__":

    print(lis([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]))
