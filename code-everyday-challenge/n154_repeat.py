
def max_sum_subarr(a):
    curr_sum, max_so_far = a[0],a[0]
    st, end  = 0,0

    for i in range(1,len(a)):
        curr_sum = max(curr_sum+a[i],a[i])

        if curr_sum == a[i]:
            st = i

        # max_so_far = max(max_so_far,curr_sum)
        if max_so_far < curr_sum:
            max_so_far = curr_sum
            end = i

    return max_so_far, a[st:end+1]



if __name__ == "__main__":
    a = [1,2,3,-2,5,-1,-3]
    a = [1,2,4,-2,5,-12,4,5,9]
    a=[-2,1,-3,4,-1,5,1,-5,4]

    print(max_sum_subarr(a))