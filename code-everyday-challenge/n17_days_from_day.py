




def solution(S, K):
    # write your code in Python 3.6
    # pass
    if K >= 7:
        K = K%7
    d = {'Sun':1,'Mon':2,'Tue':3,'Wed':4,'Thu':5,'Fri':6,'Sat':7}
    d_map = {1:'Sun',2:'Mon',3:'Tue',4:'Wed',5:'Thu',6:'Fri',7:'Sat'}

    if d[S]+K <= 7:
        return d_map[d[S]+K]
    else:
        return d_map[(d[S]+K)%7]


print(solution('Sat',23))