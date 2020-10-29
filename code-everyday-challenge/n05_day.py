#gcd

def gcd(a, b):
    if a==0:
        return b
    if b==0:
        return a
    
    bigger = max(a, b)
    smaller = min(a, b)

    remainder =bigger% smaller

    return gcd(smaller,remainder)







if __name__ == "__main__":

    a,b = map(int,input().split())
    print(gcd(a,b))