

def cons_sum(n):

    sum = 0
    i,j = 1,0
    count = 0
    while j <= n:
        # cur_sum=sum[j]-sum[i]+1
        # print(sum,i,j)
        if sum ==n:

            print([*range(i,j+1)],sum,i,j)
            count+=1
            sum = sum-i
            i = i+1
            j = j+1
            sum = sum+j 
            # print(sum)
        elif  sum < n:
            j+=1
            sum =sum+j
        else :
            sum = sum-i
            i+=1



    return count





print(cons_sum(15))

