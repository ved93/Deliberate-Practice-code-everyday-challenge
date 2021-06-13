



# def binary_search(a,k):
#     mid  = (len(a)-1)//2

#     if len(a) <= 1:
#         return a

#     if k == a[mid]:
#         return True
#     elif k < a[mid]:
#         return binary_search(a[:mid+1],k)
#     else:
#         return binary_search(a[mid+1:],k)

#     return -1 


def binary_search(a,k):
    if a ==[]:
        return False
    elif len(a) == 1:
        return a[0] == k
    else:
        mid = len(a)//2 
        if a[mid] > k:
            return binary_search(a[:mid], k)
        else:
            return binary_search(a[mid:], k)




    







if __name__ == "__main__":
    a = [1,3, 4,5, 8,9,10]
    k = 10
    print(binary_search(a,k))