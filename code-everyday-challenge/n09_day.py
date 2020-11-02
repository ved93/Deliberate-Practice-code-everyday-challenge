
def get_fibonacci_huge(m,n):
    previous=0
    current =1
    sum =0
    for i in range(2,n+1):
        previous,current =current,previous+current

        if i >=m:
            sum = sum+current

    return sum%10






if __name__ == "__main__":
    m,n = map(int, input().split())
    print(get_fibonacci_huge(m,n))