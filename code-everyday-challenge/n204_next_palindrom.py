

# https://www.geeksforgeeks.org/next-higher-palindromic-number-using-set-digits/

# def next_palindrome(num):
#         nums= [int(x) for x in num]

#         if len(num) <= 3:
#             return -1

#         from collections import Counter
#         t = Counter(nums)
#         palins =[x for x,y in t.items() if y%2 ==0]

#         palins=sorted(palins)

#         palins.remove(int(num[0]))

#         palins.append(int(num[0]))

#         st=[None]*len(nums)

#         palins.extend([x for x,y in t.items() if y%2 !=0])

#         for i in range(len(palins)):
#             # print(palins[i])
#             st[i] = palins[i]
#             st[-(i+1)] = palins[i]



#         return st

# function to reverse the digits in the
# range i to j in 'num'
def reverse(num, i, j) :
     
    while (i < j) :
        temp = num[i]
        num[i] = num[j]
        num[j] = temp
        i = i + 1
        j = j - 1
         
     
# function to find next higher palindromic
# number using the same set of digits
def nextPalin(st) :


    num = list(st)

    # print(num)
    n = len(st)

     
    # if length of number is less than '3'
    # then no higher palindromic number
    # can be formed
    if (n <= 3) :
        # print "Not Possible"
        return -1
     
    # find the index of last digit
    # in the 1st half of 'num'
    mid = n // 2 - 1
     
    # Start from the (mid-1)th digit and
    # find the first digit that is
    # smaller than the digit next to it.
    i = mid - 1
    # print(i)
    while i >= 0 :
        if (num[i] < num[i + 1]) :
            break
        i = i - 1
     
    # If no such digit is found, then all
    # digits are in descending order which
    # means there cannot be a greater
    # palindromic number with same set of
    # digits
    if (i < 0) :
        # print "Not Possible"
        return -1
     
    # Find the smallest digit on right
    # side of ith digit which is greater
    # than num[i] up to index 'mid'
    smallest = i + 1
    j = i + 2
    while j <= mid :
        if (num[j] > num[i] and num[j] <
                        num[smallest]) :
            smallest = j
        j = j + 1
     
    # swap num[i] with num[smallest]
    temp = num[i]
    num[i] = num[smallest]
    num[smallest] = temp
     
    # as the number is a palindrome,
    # the same swap of digits should
    # be performed in the 2nd half of
    # 'num'
    temp = num[n - i - 1]
    num[n - i - 1] = num[n - smallest - 1]
    num[n - smallest - 1] = temp
     
    # reverse digits in the range (i+1)
    # to mid
    reverse(num, i + 1, mid)
     
    # if n is even, then reverse
    # digits in the range mid+1 to
    # n-i-2
    if (n % 2 == 0) :
        reverse(num, mid + 1, n - i - 2)
         
    # else if n is odd, then reverse
    # digits in the range mid+2 to n-i-2
    else :
        reverse(num, mid + 2, n - i - 2)
         
         
    # required next higher palindromic
    # number
    result = ''.join(num)
     
    return result




if __name__ == "__main__":
    num = "35453"
    num = "4697557964"
    num = '399993'
    # print(list(map(int,num.split())))

    print(nextPalin(num))

