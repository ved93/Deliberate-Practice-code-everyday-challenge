
# array of sorted number, rotate a little bit
#[1,2,3,4,5,6,7,8,9,10]
# [8,9,10,1,2,3,4,5,6,7] --input 9 


def main(a,l,h,e):
    mid  = (l+h) //2

    if l > h:
        return -1

    if a[mid]==e:
        return mid

    if a[l] <= a[mid]:
        #means a is sorted till mid
        if e >= a[l] and e <= a[mid]:
            return main(a, 0, mid-1, e)
        return main(a, mid+1,h,e) 
         # If a[l..mid] is not sorted, then a[mid... r] 
    # must be sorted 
    else:
        if e >= a[mid] and e <= a[h] :
            return main(a,mid+1,h, e)
        return main(a,l ,mid-1,e)


    # return mid



if __name__ == "__main__":

    a= [8,9,10,1,2,3,4,5,6,7]

    print(main(a,0,len(a)-1,4))

