
# https://www.geeksforgeeks.org/swap-all-occurrences-of-two-characters-to-get-lexicographically-smallest-string/

def smallest_str_swap(s,n):
    MAX = 256
    i,j = 0,0

    chk  = [-1 for i in range(MAX)]

    # for i in range(MAX):
    #     chk[i] = -1

    for i in range(n):

        if chk[ord(s[i])]== -1:
            chk[ord(s[i])] = i

    for i in range(n):
        flag =False

        for j in range(ord(s[i])):

            if chk[j] > chk[ord(s[i])] :
                flag = True
                break

        if flag:
            break

    # If swapping is possible
    if (i < n):
  
        # Characters to be swapped
        ch1 = (s[i])
        ch2 = chr(j)
  
        # For every character
        for i in range(n):
  
            # Replace every ch1 with ch2
            # and every ch2 with ch1
            if (s[i] == ch1):
                s[i] = ch2
  
            elif (s[i] == ch2):
                s[i] = ch1
  
    return "".join(s)






if __name__ == "__main__":
    s = 'ccad'
    s = list(s)
    print(smallest_str_swap(s, len(s)))