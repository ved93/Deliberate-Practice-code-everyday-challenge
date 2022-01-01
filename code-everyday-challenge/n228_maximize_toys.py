
def toy_count(a,k):
    a=sorted(a)

    count = 0
    for i in range(len(a)):
        if k-a[i] >= 0:
            k = k-a[i] 
            count += 1   
        else:
            break


    return count
 





if __name__ == "__main__":
    a = [1, 12, 5, 111, 200, 1000, 10]
    K = 50 
    a = [20, 30, 50]
    K = 100
    print(toy_count(a,K))