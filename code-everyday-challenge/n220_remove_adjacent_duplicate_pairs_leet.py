
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/1046953/Python-using-stacks

def remove_adjacent_duplicates(S):
    if not S:
        return S
    res = [S[0]]
    for curr in S[1:]:            
        if res and curr == res[-1]:
            res.pop()
        else:
            res.append(curr)
    res = ''.join(res)                
    return res



def removeDuplicates( S):
    """
    :type S: str
    :rtype: str
    """
    if not S: return s
    stack = []
    for ch in S:
        if stack and stack[-1]==ch: 
            stack.pop()
            continue
        stack.append(ch)
    return "".join(stack)



if  __name__ == "__main__":
    s = 'acaaabbbacdddd'
    s = 'abccbccba'
    print(removeDuplicates(s))