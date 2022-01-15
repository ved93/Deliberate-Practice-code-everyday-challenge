
# Implement a random number generator for numbers between [0, n]. Every time the
#  generator function is called, you should return a random number. However, 
# no repetitions are allowed (i.e. you cannot return the same number twice). 
# Once you've used up all numbers, return 0.



from random import randint



# def get_no_zero_random_number(n):
#     # return randint(1, 9)
#     while True:
#         a = randint(1, n//2)
#         b = n-a
#         if '0' not in str(a) and '0'  not in str(b):
#             return [a, b]

def get_random_num(a):
    ind=randint(0, len(a)-1)
    print(a, ind)
    num  = a[ind]
    # a.remove(num)
    return num





if __name__ == "__main__":
    # print(get_no_zero_random_number(10))
    a = [2,7,1,5,8]
    for i in range(5):
        num = get_random_num(a)
        print(num)
        a.remove(num)
    # print(get_random_num(a))