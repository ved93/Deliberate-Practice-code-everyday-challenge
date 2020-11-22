
def max_prize(n):
    if n <= 1:
        return n
    left = n
    s = 0
    m = 1
    l = []
    while left >= m:
        s = s+m 
        l.append(m)
        left = left-m
        m = m+1

    l[-1] = l[-1] +left

    return (l,s)    






if __name__ == '__main__':
    print(max_prize(1))
