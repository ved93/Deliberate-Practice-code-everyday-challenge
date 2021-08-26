

def longest_common_prefix(s):
    min_st=min(s)
    common_prefix = ''
    for i,char in enumerate(min_st):

        for word in s:

            if word[i] == char:
                # common_prefix += char
                pass
            else:
                if len(common_prefix) == 0:
                    return -1
                return common_prefix

        common_prefix += char


    return common_prefix


if  __name__ == "__main__":
    s = ['geeksforgeeks', 'geeks', 'geek',
         'geezer']
    s =  ['hello', 'world']
    print(longest_common_prefix(s))