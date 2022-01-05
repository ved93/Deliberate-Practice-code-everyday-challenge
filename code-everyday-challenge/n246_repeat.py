

def search(a,f):
    
    if len(a) == 0:
        return -1

    # print()
    mid = len(a)//2
    l,r = 0 , len(a)-1

    while l <= r:
        mid = (l+r)//2

        if a[mid] < f:
            l = mid+1 

        elif a[mid] > f:
            r = mid-1
        else:
            return mid  












if __name__ == "__main__":
    import random
    random.seed(123) 
    a = random.sample(range(1,50),6)
    f = 4
    a = sorted(a)

    print(a)

    print(search(a,f))