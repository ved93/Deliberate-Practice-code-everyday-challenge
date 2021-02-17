
def solve(a):
    step = 0
    for i in range(1,len(a)-1):
        if a[i] == a[i-1] and a[i] == a[i+1]:
            pass 
        # elif a[i] == a[i-1] and a[i] == a[i+1]:
        elif a[i] >= a[i-1] and a[i] <= a[i+1]:
            # if a[i] == a[i+1]:
            pass
            # else:



        elif a[i] >= a[i-1] and a[i] > a[i+1]:
            diff = a[i] - a[i+1]
            if a[i] - diff < a[i-1]:
                pass
            else:
                a[i]=a[i] - diff
                step +=diff
        elif a[i] < a[i-1] and a[i] <= a[i+1]:
            diff = a[i-1] - a[i]
            a[i]=a[i] + diff
            step +=diff

        elif a[i] < a[i-1] and a[i] > a[i+1]:
            diff1 = a[i-1] - a[i]
            diff2 = a[i] - a[i+1]
            diff = min(diff1, diff2)
            a[i]=a[i] - diff
            step +=diff
            


            #2 3 9 8 6


    print(a)

    return step

if __name__ == "__main__":
    n = 7 
    # a= [1,4,2,3,1,4,4]
    a= [1,2,1]

    print(solve(a))