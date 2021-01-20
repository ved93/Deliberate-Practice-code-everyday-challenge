


def main(x,y):
    r= round(x/y,0)

    if r < (x/y):
        return  int(r+1)
    else:
        return int(r)



if __name__ == "__main__":
    x,y=map(int,input().split())
    print(main(x,y))

