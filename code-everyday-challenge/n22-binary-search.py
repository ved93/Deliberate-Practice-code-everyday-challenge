

def binary_search(a,k):
    left, right = 0, len(a)-1
    while (left<=right):
    	mid = (left+ right)//2
    	if(a[mid]==x):
    		return mid
    	elif(a[mid]<x):
    		left = mid+1
    	else:
    		right = mid	-1
    return -1	
        



if __name__ == "__main__":
    data=[5,1,5,8,12,13,5,8,1,23,1,11]
    n = data[0]
    m = data[n+1]
    a = data[1:n+1]
    for x in data[n+2:]:
        print(binary_search(a,x))

