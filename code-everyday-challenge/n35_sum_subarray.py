


#this is wrong


def lis( A):
    T= [None]*len( A)
    prev = [None]*len( A)

    for i in range(len( A)):
        T[i] = 1
        prev[i] = -1 

        for j in range(i):
            if A[j] < A[i] and T[i] < T[j]+1:
                T[i] = T[j]+1
                prev[i] = j


    longest =max(T)
    # print(T)

    for i in range( len(A)):
        if T[i] == longest:
   
            break
    last_index = i
    # print(last_index, longest)

    store = []
    while last_index > 0 :
        store.append(last_index)

        last_index = prev[last_index]

    store.reverse()

    print(prev,store)

    return [A[i] for i in store]

  






if __name__ == "__main__":

    print(lis([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]))
