# https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
# https://leetcode.com/problems/rotate-array/discuss/487529/py3-js-5-different-simple-solutions
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/?track=md-arrays&batchId=144

def rotate_array(arr,d,n):

    # return a[D:]+a[:D]
        # def rotateArr(self,arr,d,n):
    #Your code here
    for i in range(d):
        # leftRotatebyOne(arr, n)
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i + 1]
        arr[n-1] = temp
        
    return arr




if __name__ == "__main__":
    a = [2,4,6,8,10,12,14,16,18,20]
    N= 10
    D= 3
    print(rotate_array(a,D,N))