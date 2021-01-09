


def get_last_digit_sum(n):
    if n <= 1:
        return n
    # a=[None]*n
    # a[0]=0
    # a[1]=1
    previous = 0
    current =1
    sum = 1
    for i in range(2,n+1):
        # current, previous =
        previous, current = current, (previous+current)
        sum = current+sum

    return (current%10, sum%10)






if __name__ == '__main__':
    n=int(input())
    print(get_last_digit_sum(n))