

rank1 = '23456789TJQKA'
rank2 = 'A23456789TJQK'


def flush(a, b, c, d, e):
    # a, b, c, d, e = input().split()
    # they are not same suit
    if not (a[1] == b[1] and b[1] == c[1] and c[1] == d[1] and \
        d[1] == e[1]):
        return 'NO'
    lst = []
    lst.append(a[0])
    lst.append(b[0])
    lst.append(c[0])
    lst.append(d[0])
    lst.append(e[0])

    has_A = False
    if 'A' in lst:
        has_A = True

    lst.sort(key= lambda x: rank1.index(x))
    max_value = rank1.index(max(lst, key= lambda x: rank1.index(x)))
    min_value = rank1.index(min(lst, key= lambda x: rank1.index(x)))
    if max_value - min_value == 4:
        return 'YES'
    elif not has_A:
        return 'NO'
    
    lst.sort(key= lambda x: rank1.index(x))
    max_value = rank2.index(max(lst, key= lambda x: rank2.index(x)))
    min_value = rank2.index(min(lst, key= lambda x: rank2.index(x)))
    if max_value - min_value == 4:
        return 'YES'
    return 'NO'




if __name__ == "__main__":
    # l=list(input.split())
    a, b, c, d, e = input().split()
    # l = ["AD","KH","QH","JS","TC"]
    print(flush(a, b, c, d, e ))

