















# https://www.lintcode.com/problem/386/solution/35724







def longest_k_substring(s,k):
    from collections import defaultdict

    if not s or not k:
        return -1
    
    i =j =0
    unique = defaultdict(int)
    longest = float('-inf')

    while j < len(s):
        c = s[j]
        j +=1

        unique[c]+=1

        while len(unique) > k:
            d = s[i]
            i +=1

            unique[d] -=1
            if unique[d] ==0:
                del unique[d]

            
        longest = max(longest, j-i)


    # print(len(unique))
    if len(unique) >=k:
        return longest
    else:
        return -1







if  __name__ == "__main__":
    s = 'aabacbebebe'
    k = 3

    s = 'gbwkfnqduxwfn'
    k =15
    s = 'repggxrpnrvy'
    k =12
    # s = 'hq'
    # k = 2
    print(longest_k_substring(s, k))







