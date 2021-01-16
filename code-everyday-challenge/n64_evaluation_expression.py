

def sub(s):
    # print(s)
    a = list(map(int, s.split('-')))
    print(a)
    return a[0]*2 - sum(a)

def main():
    s = input()
    add = s.split('+')
    print(add)
    print(sum(map(sub, add)))
    
    




if __name__ == "__main__":

    print(main())