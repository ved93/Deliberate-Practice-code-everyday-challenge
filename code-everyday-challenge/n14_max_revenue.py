


def max_revenue(a,c):
    a=sorted(a,reverse=True)
    c=sorted(c,reverse=True)

    s = 0
    for i in range(len(a)):
        s = s+a[i]*c[i]
    return s



if __name__ == "__main__":
    print(max_revenue([1,3,-5,-7], [-2,4,1,8]))