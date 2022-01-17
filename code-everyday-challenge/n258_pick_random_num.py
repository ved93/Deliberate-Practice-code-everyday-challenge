

# Given a list of intervals e.g. [[4,9], [12,14]], randomaly select one number from 
# any of the intervals. Each number from all the intervals should have equal probality
#  of getting selected. In the above example, output could be any number from -
#  (4,5,6,7,8,9,12,13,14) .


import random 

def random_pick(intervals):
    a = []
    for i in intervals:
        a += list(range(i[0], i[1]+1))
    print(a)
    return random.choice(a)

def random_pick_v2(intervals):
    total_length = 0
    for interval in intervals:
        total_length += interval[1] - interval[0] + 1
    print(total_length)
    pick_num = random.randint(0, total_length - 1)
    print(pick_num)
    for interval in intervals:
        if pick_num < interval[1] - interval[0] + 1:
            print(interval[0] + pick_num)
            return interval[0] + pick_num
        else:
            pick_num -= interval[1] - interval[0] + 1





print(random_pick_v2([[4,9], [12,14]]))