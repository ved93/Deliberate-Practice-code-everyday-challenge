
# https://stackoverflow.com/questions/22211521/how-to-recursively-remove-all-adjacent-duplicates/22211765

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/1046953/Python-using-stacks

# https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/


def remove_adjacent_duplicates(s):
    st = []
    prev = s[0]
    st.append(prev)
    for i in range(1, len(s)):    
        print(st)

        if st[-1] == s[i] and st:
            st.pop()
            # prev = ''
            # pass

        else:
            st.append(s[i])
            # prev = s[i]

    return  ''.join(st)



def rmv(st,i):
    if i==len(st)-1:
        return
    if not st:
        return 
    if st[i]==st[i+1]:
        tmp=st[i]
        while(i<len(st) and st[i]==tmp):
            st.pop(i)
        if not i-1:
            rmv(st,i-1)
        else:
            rmv(st,0)
    else:
        rmv(st,i+1)

    return ''.join(st)







if  __name__ == "__main__":
    s = 'abccbccba'
    # print(remove_adjacent_duplicates(s))
    print(rmv(list(s),0))