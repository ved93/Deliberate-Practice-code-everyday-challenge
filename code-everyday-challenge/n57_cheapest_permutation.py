
# def main(mat,size):
#     min_sum = 0
#     for i in range(size-1):
#         print(mat[i][i+1])



from itertools import permutations

def cost(perm, A):
    c = 0
    for i in range(len(perm)-1):
        print(perm,perm[i],perm[i+1])
        c += A[perm[i]] [perm[i+1]]
    return c

def solve(A):
    res = []
    m = 2**32
    n = len(A)
    perms = list(permutations([i for i in range(n)]))
    print(perms)
    for perm in perms:
        if cost(perm, A) < m:
            m = cost(perm, A)
            res = perm[:]
    print(' '.join([str(e+1) for e in res]))

if __name__ == "__main__":
    # size = int(input())
    # mat =[]
    # for _ in range(size):
    #     mat.append(list(map(int,input().split())))
    # print(mat) 
    mat = [[0, 1, 2], [1, 0, 4], [2, 4, 0]]
    size = 3
    # print(main(mat,size))
    print(solve(mat))
