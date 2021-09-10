


def remove_duplicates(s):
    from collections import defaultdict

    store = defaultdict(int)
    new_str = ''

    for i, char in enumerate(s):

        if char in store:
            continue
        else:
            store[char] = store[char] + 1
            new_str += char
    
    return new_str







if __name__ == "__main__":
    s = 'zvvo'
    s = 'gfgeeksgdl'
    # print(set(s))
    # from collections import OrderedDict
    # print(OrderedDict.fromkeys(s))
    print(remove_duplicates(s))