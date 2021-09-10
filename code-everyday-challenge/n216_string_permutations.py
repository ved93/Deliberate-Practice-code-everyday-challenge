


def get_permutations(s, l,r):

    if l ==  r:
        print(''.join(s))
    else:

        for i in range(l,r+1):
            s[i], s[l] = s[l], s[i]
            # print(s)
            get_permutations(s,l+1,r)

            s[i], s[l] = s[l], s[i]






if  __name__ == "__main__":
    s = 'ABC'
    l = 0
    r = len(s)-1
    s = list(s)
    print(get_permutations(s,l,r))    
