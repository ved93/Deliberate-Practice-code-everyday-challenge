

def main(x, y, z):
    a = []
    a.append(0)   
    prev = x  
    next  =x-y 
    a.extend([prev,next])   


    i = 1
    while (prev < z) and (next < z): 
        prev = next +x
        next = prev-y
        i+=1
        print(prev, next)
        a.extend([prev,next])   

    print(a)
    if (prev == z) or (next == z):
        return z
    else:
        return -1







if __name__ == "__main__":
    print(main( 2,2, 6))