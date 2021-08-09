
# https://practice.geeksforgeeks.org/problems/plus-one/1/?track=md-arrays&batchId=144#

def plus_one(a):
    if a is None:
        return -1

    d=''.join(str(x) for x in a)
    # print(d)
    new_number=int(d)+1

    d = []
    for i in str(new_number):
        d.append(int(i))

    
    

    return  d



if __name__ == "__main__":
    a = [1,2,4]
    a =  None
    print(plus_one(a))