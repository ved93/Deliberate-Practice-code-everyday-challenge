import sys
def main(a):
    max_=max(a)
    # print( (a.remove()))
    b = a.copy()   
    b.remove(max_) 
    # print(a,b)
    
    if max(b) == max_:
        count =0
        for i in range(len(a)):
            if a[i] == max_:
                count += 1
            if count == 3:
                # a.remove(a[i])

                # print()

                return a[:i]+a[i+1:]
    else:
        a.remove(max_)
        return a








if __name__ == "__main__":
    # n = int(input())
    # a=list(map(int,input().split()))    
    # print(a)
    print(main([4 ,1, 4, 2, 4, 3, 4]))