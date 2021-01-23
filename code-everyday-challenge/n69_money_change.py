
#the min coins with denom 1,5, 10 that changes m

def main(m,coins):
    result = []

    while m > 0:
        max_coins=max(c for c in coins if c <= m)
        m-=max_coins
        result.append(max_coins)

    return '+'.join(map(str, result))


if  __name__ == "__main__":
    coins = [1,5,10]
    m = 28
    print(main(m, coins))