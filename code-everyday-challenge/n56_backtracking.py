
from collections import defaultdict

def nested_fors(n,firstfor,x):
    store= [] #defaultdict(int)
    if firstfor < n:
        for x[firstfor] in ['0','1']:
            # print(x[0])
            nested_fors(n,firstfor+1, x)
    else:
        print(x)
        m = ''
        if x[0] == '1':
            m=m +'1'
            print(store)
        if x[1] == '1':
            m=m +'2'

            # store[x] =  0
        if x[2] == '1':
            m=m +'3'
            # print(m)

            # store[x] = 3   
        store.append(m)
        print(store)
        # 
    # return store  



if __name__ == '__main__':
    print(nested_fors(3,0,['']*3))


#https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm

# def toString(List): 
#     return ''.join(List) 
 
# # Function to print permutations of string 
# # This function takes three parameters: 
# # 1. String 
# # 2. Starting index of the string 
# # 3. Ending index of the string. 
# def permute(a, l, r): 
#     if l==r: 
#         print(toString(a) )
#     else: 
#         for i in range(l,r+1): 
#             a[l], a[i] = a[i], a[l] 
#             permute(a, l+1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack 
 
# # Driver program to test the above function 
# string = "ABC"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n-1) 

