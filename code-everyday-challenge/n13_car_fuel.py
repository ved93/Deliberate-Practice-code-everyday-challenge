import sys


def get_refills(d, m, n,stops):
    if m >= d:
        return 0

    min_stops = 0
    for i in range(n):
        print(stops[i])

        if stops[i] <= m and stops[i+1] <= m:
            if i+1==n-1:
                if d > m:
                    min_stops=min_stops+1
                    return min_stops


            continue
        elif stops[i] <= m and stops[i+1] > m:
            min_stops=min_stops+1
            m = m+stops[i]

            if i+1==n-1:
                if d > m:
                    min_stops=min_stops+1
                    return min_stops

        else :
            return -1


        # else:
        #     min_stops=min_stops+1
        #     m=m+stops[i-1]
        #     if i == n-2:
        #         min_stops=min_stops+1  
        #         break
    

    return min_stops




if __name__ == "__main__":
    # data=list(map(int,sys.stdin.read().split()))
    # print(data[0],data[1],data[3:])
    # print(get_refills(da ta[0],data[1],data[2],data[3:] ))
    # print(get_refills(950,400,4,[200 ,375 ,550, 750] ))
    print(get_refills(10,3,4,[1,2,5,9] ))


