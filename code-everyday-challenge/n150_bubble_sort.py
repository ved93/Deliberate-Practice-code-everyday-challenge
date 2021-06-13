

def bubble_sort_recursion(a,counter=0):
    if counter >= len(a)-1:
        return a
    prev = a[0]
    counter = 1
    for i in range(1,len(a)):
        if prev > a[i]:
            a[i-1],a[i] = a[i], a[i-1]
        else:
            counter +=1
        prev = a[i]
    
    return bubble_sort(a, counter)


def bubble_sort(a):
    swap = False
    while not swap:
        swap = True
        for i in range(1,len(a)):
            if a[i-1] > a[i]:
                a[i-1],a[i] = a[i], a[i-1]
                swap = False

    return a



    



if __name__ == "__main__":
    a=[5,1,5,8,12,13,5,8,1,23,1,11]
    print(bubble_sort(a))