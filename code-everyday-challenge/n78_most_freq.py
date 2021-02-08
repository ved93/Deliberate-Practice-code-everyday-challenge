

from collections import defaultdict

def main(q,a,b):
    d = defaultdict(int)


    q = q[a-1:b]
    for i in range(len(q)):
        d[q[i]] = d[q[i]]+1

    d=dict(sorted(d.items(), key = lambda k : (k[1],k[0]), reverse=True))
    return list(d.keys())[0]
    # print(d)











if __name__ == "__main__":
    q = "abba"
    # print(len)
    n = 6
    al = [1,2,1,2,1,2]
    bl = [1,2,2,3,1,4]
    for a,b in zip(al,bl):
        print(main(q,a,b))