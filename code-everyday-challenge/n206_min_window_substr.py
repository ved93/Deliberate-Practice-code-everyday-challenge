# https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1/?track=md-string&batchId=144

# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
# https://leetcode.com/problems/minimum-window-substring/discuss/968611/Simple-Python-sliding-window-solution-with-detailed-explanation

# https://leetcode.com/problems/minimum-window-substring/discuss/286584/Python-easy-to-understand



def minWindow(s, t):
    import collections
    need = collections.Counter(t)            #hash table to store char frequency
    missing = len(t)                         #total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):          #index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:                     #match all chars
            print(s[i],need[s[i]], need)
            while i < j and need[s[i]] < 0:  #remove chars to find the real start
                need[s[i]] += 1
                i += 1
            need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
            missing += 1                     #we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                           #update i to start+1 for next window
    # return s[start:end]
    if s[start:end]:
        return s[start:end]
    else:
        return -1


if __name__ == "__main__":
    s =  'hasjkhflaskdf' #'zoomlazapzo'
    t =   'sdlkjfshd' #"oza"
    print(minWindow(s,t))

