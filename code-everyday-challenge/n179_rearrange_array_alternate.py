# https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form/

def rearrange(a):
    temp = [None] * len(a)

    small, large = 0, len(a)-1
    flag = True

    for i in range(len(a)):
        if flag:
            temp[i] = a[large]
            large= large-1
        else:
            temp[i] = a[small]
            small= small+1

        flag = bool(1-flag)

    for i in range(len(a)):
        a[i] = temp[i]

    return a



if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    print(rearrange(a))