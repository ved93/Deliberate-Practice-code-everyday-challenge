



def order_square(a):
    right  = 0
    while right < len(a) and a[right] < 0:
        right +=1 
    left = right-1

    output = []

    while left >= 0  and right < len(a):

        if a[left]**2 < a[right]**2:
            output.append(a[left]**2)
            left -=1

        else:
            output.append(a[right]**2)
            right +=1
    

    while left >=0 :
        output.append(a[left]**2)
        left -=1

    while right  < len(a):
        output.append(a[right]**2)
        right +=1

    return output












if  __name__ == "__main__":

    a = [-4, -3, 1, 2, 4]

    print(order_square(a))