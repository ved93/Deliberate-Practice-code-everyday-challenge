

def majority_element(a,  left, right):

    if left == right:
        return -1

    if left+1 == right:
        return a[left]
    lookup = {}
    for i in a:
        if i not in lookup:
            lookup[i] =1
        else:
            lookup[i] += 1
    maximum = max(lookup.values())
    # key_l = 
    print(list(lookup.values()).index(maximum))


    if maximum > len(a)/2:
        return maximum

    return -1






if __name__ == "__main__":
    n = 5
    a = [2,3,9,2,2]

    print(majority_element(a,0,n))


