# Compute euclidean distance  between series (points) P and Q, without using a packaged formula 
# # input  
# P-> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# Q->[10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
# # desired output 
# 18.165 



import math

def distance_euclid(a,b):
    s = 0
    for i in range(len(a)):
        s= s+(a[i]-b[i])**2

        # print(s)
    return math.sqrt(s)







if __name__ == "__main__":
    p=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
    q= [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
    print(distance_euclid(p,q))
