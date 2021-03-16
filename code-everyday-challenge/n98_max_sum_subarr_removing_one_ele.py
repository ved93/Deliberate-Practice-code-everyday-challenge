
def main(a):

    curr_sum, max_so_far = a[0],a[0]
    fw =[0 for k in range(len(a))]
    bw =[0 for k in range(len(a))]
    n = len(a)

    fw[0] = curr_sum
    #for ward dir 

    for i in range(1,len(a)):
        curr_sum = max(curr_sum+a[i], a[i])

        max_so_far = max(max_so_far,curr_sum)

        fw[i] = curr_sum
    # print(max_so_far)

    curr_sum = max_so_far = bw[n-1] =a[n-1]
    i =n-2
    while i >= 0:
        # print(i)
        curr_sum = max(curr_sum+a[i], a[i])

        max_so_far = max(max_so_far, curr_sum)

        bw[i] = curr_sum
        i-= 1

    fans = max_so_far

    # print(max_so_far)

    for i in range(1,n-1):
        fans = max(fans, fw[i-1]+bw[i+1])


    return fans


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3] 
    print(main(arr))