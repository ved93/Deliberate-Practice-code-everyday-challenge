

def calc_cost(st):
    res = 0
    j = len(st)-1
    i = 0
    while i < j:

        if st[i] != st[j]:
            res+=(min(ord(st[i]), ord(st[j]))- ord('a')+1)

        i = i+1
        j = j-1

    return res



if __name__ == "__main__":
    print(calc_cost('abcdef'))