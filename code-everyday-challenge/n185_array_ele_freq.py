
from collections import defaultdict

def count_freq(a):
    d = defaultdict(int)

    for i in range(len(a)):
        d[a[i]] = d[a[i]]+1


    # frq = [None]*len(a)
    for i in range(len(a)):
        a[i] =  d[i+1]

    return a




if __name__ == "__main__":
    a = [2, 3, 2, 3, 5]
    a = [3 ,2, 2, 2, 1]
    print(count_freq(a))