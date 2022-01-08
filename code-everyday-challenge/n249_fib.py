


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-1)


def fibs(n,fib_dict):
    # fib_dict = [None]* n
    for i in range(n):
        if  i == 0:
            fib_dict[i] = 0
        elif i  == 1:
            fib_dict[i] = 1
        else:
            fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
    return fib_dict









if  __name__ == "__main__":
    import time
    start = time.time()
    fib_dict = [None]* 10

    for i in range(1,10):
        print(fibs(i, fib_dict)[i-1])
    # print(fibs(8))



    end = time.time()
    print(f"time taken {end-start}")