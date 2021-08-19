
# https://www.geeksforgeeks.org/longest-consecutive-subsequence/
# https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1/?track=md-arrays&batchId=144#



def lcs(a):
    a = sorted(a)
    prev = a[0]
    count_max, count =1,1

    for i in range(1, len(a)):
        if a[i] == prev+1:
            count += 1
            prev = a[i]
        elif a[i] == prev:
            prev = a[i]
        else:
            count_max = max(count,count_max)
            count = 1
            prev = a[i]

    return max(count,count_max)



def findLongestConseqSubseq(arr, n):
 
    s = set()
    ans = 0
 
    # Hash all the array elements
    print(arr)
    for ele in arr:
        # print(ele)
        s.add(ele)

    print(s)
 
    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):
 
         # if current element is the starting
        # element of a sequence
        if (arr[i]-1) not in s:
 
            # Then check for next elements in the
            # sequence
            j = arr[i]
            while(j in s):
                j += 1
 
            # update  optimal length if this length
            # is more
            ans = max(ans, j-arr[i])
    return ans



if  __name__ == "__main__":
    a = [2,6,1,9,4,5,3]
    # a = [1 ,2, 3, 4, 5]
    # a = [6,6,2,3,1,4,1,5,6,2,8,7,4,2,1,3,4,5,9,6]
    # print(lcs(a))
    print(findLongestConseqSubseq(a, len(a)))