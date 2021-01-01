
# You are given a string of lowercase English letters. First, remove all 
# occurrences of its first letter, e.g. "abacaba" -> "bcb". Then, return
#  the longest prefix of the remaining string which doesn't contain two 
# different letters. The initial string is at least 5 and no more than 
# 100000 characters long.

def main(st):
    char=st[0]
    for i in range(len(st)):
        if char ==st[i]:
            st=st.replace(st[i],'')

            # print(st)
        break
    char = st[0] 
    for i in range(len(st)):
        if char !=st[i]: 
            return st[:i+1]




if __name__ == "__main__":
    print(main("abacaba" ))