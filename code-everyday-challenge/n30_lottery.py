import sys

def find_segments(starts, ends, points):
    l={}
    for i,j in zip(starts,ends):
        for p in points:
            if p >= i and  p <= j:
                # print(i,j,p)
                l[p] = 1
                points.remove(p)

                # l.append(1)
            else:
                l[p] = 0

                # l.append(0)


    return list(l.values())



if __name__ == '__main__':
    # input=sys.stdin.read()
    # data = list(map(int,input.split()))
    # n = data[0]
    # m= data[1]
    # starts = data[2:2 * n + 2:2]
    # ends   = data[3:2 * n + 2:2]
    # points = data[2 * n + 2:]
    starts = [0, 7]  
    ends=   [5, 10]
    points= [1, 6, 11]

    print(starts, ends, points)
    print(find_segments(starts,ends,points))


