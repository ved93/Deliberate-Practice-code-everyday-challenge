# input m strings consisting of letters a and b only and integer n
# output: a string s of length n containing each si(for all 1<=i<=m) as
#  a substring.


# store= [] #defaultdict(int)

def nested_fors(n,firstfor,x,store = []):
    # global store
    if firstfor < n:
        for x[firstfor] in ['a','b']:
            # print(x[0])
            nested_fors(n,firstfor+1, x)

            # print(''.join(g))
            # print(st)
            # store.append(x)

    else:
        b= ''.join(x)
        if ('bab' in b) and ('abb' in b):
            print('stop', b)
        # store.append(x)
        # print(store)
    
    # return store

print(nested_fors(4,0,['']*4))


# def main(s):


#     return 0


# if __name__ == "__main__":
#     n,m,s1,s2 = 4,3, 'bab','abb'
#     print(main(n,m,s1,s2))