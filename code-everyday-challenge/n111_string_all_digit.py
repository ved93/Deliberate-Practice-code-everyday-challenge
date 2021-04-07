
def isDigit(ch):
    ch = ord(ch)
    if (ch >= ord('0') and ch <= ord('9')):
        return True
    return False


def all_digits(st,n):
    present = [False for i in range(MAX)]

    for i in range(n):
        # If the current character is a digit
        if (isDigit(st[i])):
  
            # Mark the current digit as present
            digit = ord(st[i]) - ord('0')
            present[digit] = True
  
    # For every digit from 0 to 9
    for i in range(MAX):
  
        # If the current digit is
        # not present in st
        if (present[i] == False):
            return False
  
    return True

if __name__ == "__main__":
    MAX= 10 

    st = 'nfnrjfek6327655hwidhedk'

    print(all_digits(st,len(st)))