
# https://www.techiedelight.com/rearrange-array-positive-negative-numbers-alternate-positions/

# https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

# https://www.careercup.com/question?id=5741006670528512


def arrange_alternate(a):

    pos, neg = [],[]
    for i in range(len(a)):

        if a[i] >= 0:
            pos.append(a[i])
        else:
            neg.append(a[i])

    i,j,k = 0,0,0
    while i < len(pos) and j < len(neg):

        # a[i]pos[i])
        # a.append(neg[j])
        a[k] = pos[i]
        a[k+1] = neg[j]

        k +=2

        i += 1
        j+=1


    while i < len(pos):
        a[k] = pos[i]
        k +=1
        i += 1

    while j < len(neg):
        a[k] = neg[j]
        k +=1
        j += 1

    
    return a



def rearrange(arr, n):
    # sort the array
    arr.sort()

    # print(arr)
 
    # initialize two pointers
    # one pointing to the negative number
    # one pointing to the positive number
    i, j = 1, 1
    while j < n:
        if arr[j] > 0:
            break
        j += 1
 
    # swap the numbers until the given condition gets satisfied
    while (arr[i] < 0) and (j < n):
        # swaping
        arr[i], arr[j] = arr[j], arr[i]  
         
        # increment i by 2
        # because a negative number is followed by a positive number
        i += 2     
        j += 1
     
    return(arr)










if __name__ == "__main__":
    a = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    # print(arrange_alternate(a))
    print(rearrange(a, len(a)))
