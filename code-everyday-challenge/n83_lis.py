

def solve(A):
    T = [None]*len(A)
    prev = [None]*len( A)

    for i in range(len(A)):
        T[i] = 1
        prev[i] = -1

        for j in range(i):
            
            if A[j] < A[i] and T[i] < T[j]+1:
                T[i] = T[j]+1


    return max(T[i] for i in range(len(A))) 








if __name__ == '__main__':
    A = [5,3,2,4,6,1]
    print(solve(A))