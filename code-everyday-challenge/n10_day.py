
def get_fibonacci_huge(n):
    if n <= 1:
        return n

    previous = 0
    current =1
    sum = 1
    for __ in range(2,n+1):
        previous,current = current, previous+current

        sum = sum+(current*current)
        # print(sum, '  ', current*current)
    return sum%10


if __name__ == '__main__':
    n  = int(input())
    print(get_fibonacci_huge(n))
    