


def main(a,l,h,key):
    mid  = (l+h) // 2

    if l > h:
        print(l,h)
        return -1

    if a[mid] == key:
        return mid

    if a[l] <= a[mid]:
        #means left half is sorted
        # print('left me',l,h, a[l:h+1] ,mid)
        if a[mid] >= key and a[l] <= key:
            return main(a,l, mid-1, key )
        return main(a, mid+1,h, key)  

    else:
        #right sorted
        print('here', l,h)
        if a[mid] <= key and key <= a[h]:
            return main(a,mid+1,h, key)
        
        return main(a,l, mid-1, key)




if __name__ == "__main__":

    a= [8,9,10,1,2,3,4,5,6,7]

    print(main(a,0,len(a)-1,8))
