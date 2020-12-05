
# find longest increasing sequence
def find_lis(A):
    T = [None]*len(A)
    prev = [None]*len(A)

    for i in range(len(A)):
        T[i] = 1
        prev[i] = -1
        for j in range(i):
            print(i,j,T, T[i])
            if A[j] < A[i] and T[i] < T[j]+1:
                T[i] = T[j] + 1


    return max(T[i] for i in range(len(A)))







if __name__ =='__main__':
    a= [7, 2, 1, 3, 8, 4, 9, 1, 2, 6]
    # a= [1, 7,2, 3, 8, 4, 9 ]


    print(find_lis(a))