



# Maximum sum of contiguous subarray

def get_sum_conti_arr(a):
    n = len(a)
    curr_sum = a[0]
    max_so_far = a[0]

    end_index = 0
    for i in range(n):
        curr_sum = max(curr_sum+a[i], a[i])

        if curr_sum > max_so_far:
            max_so_far = max(max_so_far,curr_sum)
            end_index = i

    start_index = end_index
    while start_index > 0:
        if max_so_far < 0:
            break
        start_index-=1


    return max_so_far, (start_index+1,end_index+1)





if __name__ == "__main__":
    a = [-13, 3, 25, 20, -3, 0, 2, 17, 5, 22, -15, -4, -7]
    print(sum(a[1:10]))
    print(get_sum_conti_arr(a))