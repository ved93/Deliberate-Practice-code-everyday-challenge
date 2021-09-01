
# https://practice.geeksforgeeks.org/problems/implement-strstr/1/?track=md-string&batchId=144#
# https://leetcode.com/problems/implement-strstr/discuss/13255/Python-56-ms-Time-O(N*M)-Space-O(1)




def get_str(haystack,needle):
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    
    return -1



if  __name__ == "__main__":
    s = 'geeksforgeeks'
    x = 'for'
    print(get_str(s, x))