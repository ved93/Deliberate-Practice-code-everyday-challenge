

def check_prime(num):
    if num > 1:

        for i in range(2, (num//2)+1):

            if num % i == 0:
                print('not prime')

                break
                
        print('prime')

    else:

        print(num, "is not a prime number")



if __name__ == "__main__":

    print(check_prime(11))