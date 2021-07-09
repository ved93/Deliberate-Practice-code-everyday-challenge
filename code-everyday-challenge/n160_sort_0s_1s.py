# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.



def sort_zero_one_two(a):

    zeroes,ones,twos = 0,0,0
    for i in range(len(a)):
        if a[i]==0:
            zeroes +=1
        if a[i]==1:
            ones +=1
        if a[i]== 2:
            twos +=1

    
    return [0]*zeroes+[1]*ones+[2]*twos






if __name__== "__main__":
    a = [0,2,1,2,0]

    print(sort_zero_one_two(a))
