import sys


def get_refills(d, m, n,stops):
    if m >= d:
        return 0

    min_stops = 0
    prev_stops = 0 
    next_max_d = m
    for i in range(n-1):
        # print(stops[i])
        if prev_stops+m < stops[i]:
            return -1
        prev_stops = stops[i]

        #if its 2nd last stop
        # if i==n-1:
        #     if stops[i+1] < d



        if stops[i] <= next_max_d and stops[i+1] <= next_max_d:
            if i==n-1:
                if d-stops[i+1]<= m :
                    if d-stops[i+1] > next_max_d:
                        min_stops=min_stops+1
                    else:
                        return min_stops                    
                else:
                    return -1

            continue
        elif stops[i] <= next_max_d and stops[i+1] > next_max_d:
            min_stops=min_stops+1
            next_max_d = m+stops[i]

            if i==n-1:
                if d-stops[i+1]<= m :
                    if d > next_max_d:
                        min_stops=min_stops+1
                    else:
                        return min_stops  
                else:
                    return -1

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


