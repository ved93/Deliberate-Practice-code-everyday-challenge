


def is_prime(n):
    if n <= 1:
        return False

    x = 2
    while x*x <= n:
        if n % x ==0:
            return False 
        x +=1
    return True


if  __name__ == "__main__":
    print(is_prime(5))