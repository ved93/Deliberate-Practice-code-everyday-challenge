
# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/


def move_negative_numbers(a):
    left, right = 0, -1

    # for i in range(len(a)):
    while left < len(a)/2:
        if a[left] < 0 and a[right] < 0:
            left +=1
        elif a[left] < 0 and a[right] > 0:
            left +=1
            right -=1
        elif a[left] > 0 and a[right] > 0:
            right -=1
        elif a[left] > 0 and a[right] < 0:
            a[left], a[right] = a[right], a[left]

    return a

if __name__ == "__main__":
    a =  [-1, 2, -3, 4, 5, 6, -7, 8, 9] #[-12, 11, -13, -5, 6, -7, 5, -3, -6]
    print(move_negative_numbers(a))