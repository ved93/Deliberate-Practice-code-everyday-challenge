

def compress_str(s):
    """
    Compress a string by replacing consecutive duplicate characters with a count
    of the number of characters followed by the character.
    """
    if not s:
        return s
    compressed_str = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed_str.append(str(count))
            compressed_str.append(s[i-1])
            count = 1
    compressed_str.append(str(count))
    compressed_str.append(s[-1])
    return ''.join(compressed_str)

def compress_str_v1(s):
    curr= s[0]
    s1 = ''
    c = 1
    for i in range(0,len(s)-1):

        if (s[i] == s[i+1]):
            c = c+1
            # curr = s[i]
        else:
            if c > 1:
                s1 = s1+s[i]+str(c)
                c = 1
            else:
                s1= s1+s[i]
                c = 1
    if c > 1:
        s1 = s1+s[i]+str(c)
    else:
        s1 = s1+s[i]

    print(s1)



# Input - aaabbcccccdeabbb

# Output - a3b2c5deab3


if  __name__ == "__main__":
    s =  'aaabbcccccdeabbb'
    print(compress_str_v1(s))