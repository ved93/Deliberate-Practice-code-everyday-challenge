# Find the duplicate entries (2nd occurrence onwards) in the given numpy
#  array and mark them as True. First time occurrences should be False. 
# # Input 
# [0,0,3,0,2,4,2,2,2] 
# # Desired output 
# [False  True False  True False False  True  True  True  True] 


def get_duplicate_transform(a):
    from  collections import defaultdict
    d = defaultdict(int)
    f = [None]*len(a)

    for i in range(len(a)):
        
        if a[i] in d:
            f[i] = True
        else:
            d[i] = a[i]
            f[i] = False

    return f



if __name__ == "__main__":
    a = [0,0,3,0,2,4,2,2,2] 
    print(get_duplicate_transform(a))
