
#https://leetcode.com/problems/break-a-palindrome/discuss/892711/Python-Solution.-Readable.-simple-code.#

#https://leetcode.com/problems/break-a-palindrome/discuss/907823/Very-simple-python-solution-O(N)-time-and-space


def breakPalindrome(self, palindrome):
    """
    :type palindrome: str
    :rtype: str
    """ 
    p1 = 0
    p2 = len(palindrome)-1
    new_pal = list(palindrome)
    while p1 < p2:
        if new_pal[p1] != "a":
            new_pal[p1] = "a"
            return "".join(new_pal)
        p1+=1
        p2-=1
    if len(new_pal) == 1: return ""
    new_pal[-1] = "b"
    return "".join(new_pal)

