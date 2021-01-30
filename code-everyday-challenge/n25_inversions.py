
def get_inversions_simple(a,n):

    total = 0
    for i in range(n):

        cnt = 0
        for j in range(i,n):
            if a[i] > a[j]:
                cnt+= 1

        total += cnt

    return total

def merge_count_split_inversion(left, right):
    result = []
    count =0
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            count+=len(left)-i
            j+=1
    result.append(left[i:])
    result.append(right[j:])

    return result, count

#http://mijkenator.github.io/2016/12/10/2016-12-10-mergesort-inversion-count/
        
def count_inversions(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)


    









if __name__ == "__main__":
    # Driver Code 
    arr = [1, 20, 6, 4, 5] 
    n = len(arr) 
    print("Number of inversions are", 
                get_inversions(arr, n)) 