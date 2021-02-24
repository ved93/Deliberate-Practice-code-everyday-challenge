

def search(a,l,h, key):
    if l > h:
        return -1

    mid = (l+h)//2 

    if key == a[mid]:
        return mid

    if a[l] <= a[mid]:
        #part is sorted

        if key > a[l] and a[mid] >= key:
            return search(a,l,mid-1,key)
        return search(a,mid+1,h,key) 

    else:
        #means other part is sorted
        if key >= a[mid] and key <= a[h]:
            return search(a,mid+1,h, key)
        return search(a,l,mid-1,key)








if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
    key = 6
    i = search(arr, 0, len(arr)-1, key) 
    if i != -1: 
        print ("Index: % d"% i) 
    else: 
        print ("Key not found") 