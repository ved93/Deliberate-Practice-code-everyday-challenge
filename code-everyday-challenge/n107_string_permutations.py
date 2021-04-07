#abc, bac, cab,, acb,bca, cba,  

# Time Complexity: O(n*n!) Note that there are n! permutations and it requires O(n) time to print a a permutation.

def main(s,l,r):

    if l == r:
        print(''.join(s))
    
    else:

        for i in range(l,r+1):
            s[i],s[l] = s[l],s[i]

            main(s,l+1,r)

            #backtrack
            s[i],s[l] = s[l],s[i]
            






if __name__ == "__main__":
    s= 'abc'
    l = 0
    r = len(s)-1
    s = list(s)
    print(main(s,l,r))