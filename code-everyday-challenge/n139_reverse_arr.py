



# def reverseList(a,l,r):
#     while l< r:
#         a[l],a[r]= a[r], a[l]
#         l = l+1
#         r = r-1

#     return a
        
#recursive

def reverseList(a,l,r):

    if l>= r:
        return a

    a[l],a[r]= a[r], a[l]
    reverseList(a,l+1,r-1)




A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

