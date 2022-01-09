

# Given two sorted arrays, fid the number of elements incommon.The arrays are the same length
# and each has all distinct elements.

def common_ele_sorted_arr(a,b):
    from collections import defaultdict
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    c = 0
    for j in b:
        if j in d:
            c += 1
    return c 

# def common_ele_sorted_arr


if __name__ == "__main__":
    a = [13,27,35,40,49,55]
    b = [17,35,39,40,55,60]
    print(common_ele_sorted_arr(a,b))
