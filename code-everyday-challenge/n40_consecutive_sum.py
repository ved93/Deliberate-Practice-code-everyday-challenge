

def cons_sum(n):

    sum = 0
    i,j = 0,0
    count = 1
    while j <= n:
        # cur_sum=sum[j]-sum[i]+1
        if sum ==n:
            count+=1
            sum = sum-i
            i = i+1
            j = j+1
            sum = sum+j 
        if  sum < n:
            j+=1
            sum =sum+j
        else :
            i+=1
            sum = sum-i


    return count





print(cons_sum(21))