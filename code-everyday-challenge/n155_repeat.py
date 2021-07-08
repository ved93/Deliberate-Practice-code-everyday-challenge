
def permute(a,l,r):

    if l == r:
        print(''.join(a))
    else:
        
        for i in range(l,r+1):
            a[i],a[l] = a[l], a[i]

            permute(a,l+1,r)

            a[i],a[l] = a[l], a[i]





if __name__ == "__main__":
    st = 'abc'
    st  = list(st)
    l = 0
    r = len(st)-1
    print(permute(st,l,r))