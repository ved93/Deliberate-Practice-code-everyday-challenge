#last digit of large fibonancci numbers
def last_digit(num):
    l = [None]*num
    l[0] =1
    l[1] =1
    for i in range(2,num):
        l[i] =(l[i-1]+l[i-2])%10


    return l[num-1] 






if __name__ == "__main__":
    num = 4543
    print(last_digit(num))