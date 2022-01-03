# Have the function ArrayChallenge(arr) read the array of integers stored in arr which will be in the following format: [K, r1, r2, r3, ...] where K represents the number of desks in a classroom, and the rest of the integers in the array will be in sorted order and will represent the desks that are already occupied. All of the desks will be arranged in 2 columns, where desk #1 is at the top left, desk #2 is at the top right, desk #3 is below #1, desk #4 is below #2, etc. Your program should return the number of ways 2 students can be seated next to each other. This means 1 student is on the left and 1 student on the right, or 1 student is directly above or below the other student.

# For example: if arr is [12, 2, 6, 7, 11] then this classrooms looks like the following picture:



# Based on above arrangement of occupied desks, there are a total of 6 ways to seat 2 new students next to each other. The combinations are: [1, 3], [3, 4], [3, 5], [8, 10], [9, 10], [10, 12]. So for this input your program should return 6. K will range from 2 to 24 and will always be an even number. After K, the number of occupied desks in the array can range from 0 to K.
# Examples
# Input: [6, 4]
# Output: 4
# Input: [8, 1, 8]
# Output: 6


def seating_students(a):
    num= a[0]

    a.remove(a[0])
    even_cnt, odd_cnt = 0,0

    for i in range(1,num-1):

        if i%2 == 0:
            even_cnt +=1
        else:
            odd_cnt +=1

    total_ways = even_cnt+2*odd_cnt+1

    discarded = 0
    prev = 999
    for i in a:

        # if i in  [1,2,num-1, num]:
        #     discarded +=2
            # continue
        if abs(i-prev) == 1:
            if i%2 ==0:
                even =i
                odd = prev
            else:
                odd=i
                even = prev

            if even > odd:
                discarded+=1
            else:
                discarded+=3
        
        elif i in  [1,2,num-1, num]:
            discarded +=2
        else:
            discarded +=3
        






    return total_ways,discarded






if __name__ == "__main__":
    a = [8, 1, 8]
    a = [6,4]
    a = [12, 2, 6, 7, 11]
    print(seating_students(a))





