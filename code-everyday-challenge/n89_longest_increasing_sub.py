

def solve(a):
    T=[None]*(len(a))
    prev = [None]*(len(a))

    for i in range(len(a)):
        T[i] = 1
        prev[i] = -1
        for j in range(i):

            if a[j] < a[i] and T[i] < T[j]+1:
                T[i] = T[j]+1

    return max(T[i] for i in range(len(a)))





if __name__ == '__main__':
    A = [5,3,2,4,6,1]
    print(solve(A))