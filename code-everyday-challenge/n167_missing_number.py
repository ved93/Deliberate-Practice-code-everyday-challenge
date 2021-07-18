
#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1/?track=MD-Math&batchId=144

# https://www.geeksforgeeks.org/find-the-missing-number-in-a-sorted-array/

def get_missingNo(A,n):
    # n = len(A)
    total = (n + 1)*(n )/2
    sum_of_A = sum(A)
    return total - sum_of_A



if __name__ == "__main__":
    a = [1, 2, 4, 6, 3, 7, 8]
    n = 8
    print(get_missingNo(a,n))