


from datetime import datetime, timedelta
from typing import List

def daterange(start_date, end_date):
    delta = timedelta(hours=1)
    while start_date < end_date:
        yield start_date
        start_date += delta

def parse_string_to_datetime(date_string: str) -> datetime:
    #  helper method to transform string into datetime
    # example: parse_string_to_datetime("2018-01-01 00:00") == datetime(2018, 1, 1)
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    

def solution(start_time: str, end_time: str, root_directory: str):
    # write your code in Python
    a = []
    for i in daterange(parse_string_to_datetime(start_time),parse_string_to_datetime(end_time)+timedelta(hours=1)):
        a.append('{}/year={}/month={}/day={}/hour={:02d}'.format(root_directory,i.year, i.month,i.day ,i.hour))
        # print(i.year, i.month, i.hour)

    return a


print(solution('2018-01-01 00:00', '2018-01-02 01:00', 'Contract'))


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