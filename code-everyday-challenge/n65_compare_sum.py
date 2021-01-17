

def main(a,b):
    sa = round(sum(a),3)
    sb = round(sum(b),3)
    if sa == sb:
        print('SUM(A)=SUM(B)')
    elif sa > sb:
        print('SUM(A)>SUM(B)')
    else:
        print('SUM(A)<SUM(B)')


    # return 0



if __name__ == '__main__':
    n = 2
    a1 = [1.500, 1.500] 
    a2= [1.000, 2.000]
    print(main(a1,a2))

