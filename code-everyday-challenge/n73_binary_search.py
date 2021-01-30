
def main(a,x):
    n=len(a)
    # mid = n//2
    left, right= 0 , n-1
    while left <= right:
        mid = (left+right)//2 
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid+1        
        else:
            right = mid-1

    return -1






if __name__ == "__main__":
    data=[1, 5, 8, 12, 13]
    print(main(data, 13))