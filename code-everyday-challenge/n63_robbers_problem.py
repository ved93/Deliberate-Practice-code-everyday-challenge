# https://www.coursera.org/learn/competitive-programming-core-skills/lecture/wSCUn/defining-solution-set

#input: n items with given weights w, w2, w3 and costs c1, c2 etc 
# largest total cost of thetems whose total weights doesnt exceed W.


store= [] #defaultdict(int)

def nested_fors(n,firstfor,x):
    global store
    # global w_total, c_total
    w_total= 0
    c_total = 0
    n= 3
    W=5
    w =[3,2,5]
    c = [2,3,6]

    if firstfor < n:
        for x[firstfor] in ['0','1']:
            # print(x[0])
            nested_fors(n,firstfor+1, x)
    else:
        # print(x)
        m = ''
        if x[0] == '1':
           w_total += w[0]  
           c_total += c[0]             

        if x[1] == '1':
            # m=m +'2'
           w_total += w[1]     
           c_total += c[1]             

            # store[x] =  0
        if x[2] == '1':
            # m=m +'3'
           w_total += w[2]
           c_total += c[2]             


            # print(m)

            # store[x] = 3   
        store.append(w_total)
        print(w_total,c_total,store)
        # 
    # return store  



if __name__ == '__main__':
    print(nested_fors(3,0,['']*3))




# def main(n,c,w,W):

    

#     return 0


# if __name__ == "__main__":
#     n= 3
#     W=5
#     w =[3,2,5]
#     c = [2,3,6]
#     print(main(n,c,w,W))