



def selection_sort(a):

    start  = 0
    while start != len(a):
        for i in range(start, len(a)):
            if a[i] < a[start]:
                a[start],a[i] = a[i], a[start]

        start +=1
    return a




if __name__ == "__main__":
    a=[5,1,5,8,12,13,5,8,1,23,1,11]
    print(selection_sort(a))