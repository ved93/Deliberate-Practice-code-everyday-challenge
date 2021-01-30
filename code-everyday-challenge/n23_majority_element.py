

def majority_elementv2(a,  left, right):

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


def get_majority_elementv2(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    count = j = 0
    for i in range(1, len(a)):
        print(a[i], '  ', a[i - 1], '  ',count)
        if a[i] != a[i-1]:
            if count < i-j:
                count = i-j
            j = i
    if count > len(a)/2:
        return count
    return -1





from collections import defaultdict

def majority_element(a,left,right):
    lookup = defaultdict(int)
    for i in range(len(a)):
        lookup[a[i]] += 1 

        if lookup[a[i]] >= len(a)/2:
            return 1

    return 0








if __name__ == "__main__":
    n = 7
    a = [1,2,3,9,2,2,2]
    # a = [1,2,3,4]

    print(get_majority_elementv2(a,0,n))


