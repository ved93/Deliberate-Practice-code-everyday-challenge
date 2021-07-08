


def move_positive(a):
    left, right = 0, len(a)-1

    while left < right:
        if a[left] < 0 and a[right] > 0:
            left = left + 1
            right = right - 1
        elif a[left] > 0 and a[right] < 0:
            a[left], a[right] = a[right], a[left]
            left = left + 1
            right = right - 1
        elif a[left] > 0 and a[right] > 0:
            right = right -1
        else:
            left = left + 1
    
    return a



if __name__ == "__main__":
    a = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    print(move_positive(a))