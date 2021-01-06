# https://www.coursera.org/learn/competitive-programming-core-skills/lecture/wSCUn/defining-solution-set


#input : array 
#the largest possible sum of subarray . a could be negative


def main(a):
    store = []
    index = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            # print(a[i:j+1])
            # store[sum(a[i:j+1])] = [i,j]
            store.append(sum(a[i:j+1]))
            index.append([i,j])




    return store,index


if __name__ == "__main__":
    a = [4,1,-2,3,-10,5]
    # print(main(a))
    store,index =main(a)
    print(index[store.index(max(store))])




