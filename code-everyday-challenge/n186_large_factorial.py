
from collections import defaultdict

def fact(x,d):

    if x <= 1:
        return 1

    if x in d:
        return d[x]
    else:
        d[x] = fact(x-1,d)*x

    return d
    

    



if __name__ == "__main__":
    a = [0, 1, 2, 3, 4]
    mod = 1000000007
    d = defaultdict(int)
    for x in a:
        print(fact(x,d))