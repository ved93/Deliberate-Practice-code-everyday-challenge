


def main(a):
    s= 0.0
    if len(a) <= 1:
        return s+round(a[0]+(1/a[0]),10)
        
    for i in a:
        s= s+round((i+1/i),10)

    return s


if __name__ == "__main__":
    # a= [-2, -3, 1, 2]
    a = [-4]
    print(main(a))