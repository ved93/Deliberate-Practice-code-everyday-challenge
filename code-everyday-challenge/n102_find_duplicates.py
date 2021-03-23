from collections import defaultdict


def findDuplicate(arr, n): 
  
    # Initialize all the elements 
    # of the countArr to 0 
    countArr = [0] * (n + 1) 
  
    # Count the occurences of each 
    # element of the array 
    for i in range(n + 1): 
        countArr[arr[i]] += 1
  
    a = False
  
    # Find the element with more 
    # than one count 
    for i in range(1, n + 1): 
        if(countArr[i] > 1): 
            a = True
            print(i, end = " ") 
  
    # If unique elements are there 
    # print "-1" 
    if(not a): 
        print(-1) 


def main(a):
    # print(dict(a))
    d = defaultdict(int)
    for e in a:
        if e in d:
            print(e)
        d[e] = d[e]+1



if __name__ == "__main__":
    a = [3, 1, 3, 4, 2]
    print(main(a))