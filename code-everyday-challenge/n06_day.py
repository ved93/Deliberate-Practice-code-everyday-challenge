

def lcm_fast(a, b):
    product = a * b
    gcd = gcd_fast(a, b)

    return product // gcd

def gcd_fast(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    bigger = max(a, b)
    smaller = min(a, b)
    reminder = bigger % smaller

    return gcd_fast(smaller, reminder)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    a, b = map(int, input().split())

    print(lcm_fast(a, b))