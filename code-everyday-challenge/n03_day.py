#fibbonancci numvers

def fibonancci(n):
    if n <= 1:
        return 1


    l = [None]*(n+1)
    # l[:n] = 0*(n)
    l[0]= 0
    l[1] = 1
    # print(l)

    for i in range(2,n+1):
        l[i] = l[i-1]+l[i-2]
        print(l)


    return l[n+1]

def fib_rec(n):
    if n <= 1:
        return n
    print(n)
    return fib_rec(n-1)+fib_rec(n-2)





if __name__ == "__main__":

    n = int(input())

    print(fib_rec(n))