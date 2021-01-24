
#largets number that can be obtained by concatenating the digits

def main():
#    a= list(map(int,input().split()))
    a = [2,3,9,3,2]
    result = []
    while len(a) > 0:
        max_d = max(a)
        a.remove(max_d)
        result.append(max_d)

    return ''.join(map(str, result))






if __name__ == "__main__":
    print(main())