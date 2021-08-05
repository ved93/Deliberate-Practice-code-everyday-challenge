
def sort012(a):

    zeroes, ones, twos =0,0,0
    for i in a:
        if i == 0:
            zeroes +=1
        if i == 1:
            ones +=1
        if i == 2:
            twos +=1

    
    # return [0]*zeroes +[1]*ones +[2]*twos

        # Store all the 0s in the beginning
    i=0
    while (zeroes > 0):
        a[i] = 0
        i+=1
        zeroes-=1
     
    # Then all the 1s
    while (ones > 0):
        a[i] = 1
        i+=1
        ones-=1
     
    # Finally all the 2s
    while (twos > 0):
        a[i] = 2
        i+=1
        twos-=1







    return a



a= [0,2, 1, 2, 0]
a= [0,0,0, 0,2,0,2]

print(sort012(a))
