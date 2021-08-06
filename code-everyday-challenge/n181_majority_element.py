# https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1/?track=md-arrays&batchId=144#

from collections import defaultdict

def majority_element(a):
    d = defaultdict(int)

    # print(d)


    for i in range(len(a)):

        d[a[i]] = d[a[i]]+1 

    # print(max(d.values()))

    if max(d.values()) > len(a)/2:
        return max(d, key = d.get)

    else:
        return -1




if __name__ == "__main__":
    a = [3,1,3,3,2]
    a = [1,13]
    print(majority_element(a))