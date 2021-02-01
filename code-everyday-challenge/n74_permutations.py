


def permute(a,l,r):
    n = len(a)
    if l ==r:
        # return a
        print(''.join(a))
    else:
        for j in range(l,r+1):

            a[j],a[l] = a[l], a[j]

            # print(a,l,j)
            permute(a,l+1,r)

            a[j],a[l] = a[l], a[j]
            # print('after',a,l,j)


        # print(a)


a = 'abc'
a= list(a)
# print(a)
# permute(a,0,len(a)-1)



### Anotherr way--  this is done in backtracking.py. Check this file
# when you need all possible combinations

# https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm

def nested_fors(n,firstfor,x):
    store = []

    if firstfor < n:
        for x[firstfor] in ['a', 'b','c']:
            nested_fors(n,firstfor+1,x)
    else:
        print(x)



nested_fors(3,0,['']*3)