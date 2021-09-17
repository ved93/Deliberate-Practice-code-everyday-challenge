
# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
# https://www.techiedelight.com/activity-selection-problem/



def activity_select(start, end,n):
    prev = 0
    next = 1
    count = 1

    store=dict(zip(start,end))
    print(sorted(store), 'here ')

    sorted_store= sorted(store.items(),key = lambda kv:(kv[1],kv[0]))
    print(sorted_store)
    sorted_store = dict(sorted_store)
    # return sorted_store
    start=list(sorted_store.keys())
    end = list(sorted_store.values())

    # return start
    # print(start)
    # print(end)

    # while next < n:
    #     prev_dur = end[prev]-start[prev]
    #     next_dur = end[next]-start[next]
    #     # print(prev, next, n,' before')
    #     if start[next]-end[prev] >0:
    #         # print(start[next],end[prev])
    #         prev = next
    #         next= prev +1 
    #         count +=1
    #         # print(prev, next, n)

    #     elif prev_dur > next_dur:
    #         prev +=1
    #         next +=1
    #     else:
    #         next +=1

    i = 0

        # Consider rest of the activities
    for j in range(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if start[j] > end[i]:
            # print j,
            count +=1
            i = j

        
        
    return count


# Activity selection problem
def selectActivity(activities):

    
    # store=dict(zip(start,end))

    # activities= sorted(store.items(),key = lambda kv:(kv[0],kv[1]))
    
    m = activities
    # `k` keeps track of the index of the last selected activity
    k = 0
 
    # set to store the selected activities index
    out = [] #set()
    print(out)
 
    # select 0 as the first activity
    if len(activities):
        out.append(0)
 
    print(activities)
    # sort the activities according to their finishing time
    activities.sort(key=lambda x: x[1])
 
    # start iterating from the second element of the
    # list up to its last element
    for i in range(1, len(activities)):
 
        # if the start time of the i'th activity is greater or equal
        # to the finish time of the last selected activity, it
        # can be included in the activities list
 
        if activities[i][0] > activities[k][1]:
            out.append(i)
            k = i            # update `i` as the last selected activity
 
    # print(out)
    return len([m[i] for i in out])




if __name__ == "__main__":
    start = [1, 3, 2, 5]
    end = [2, 4, 3, 6]
    # start = [2,1]
    # end = [2,2]
    # start = [7,2,2,3]
    # end =[8,4,7,10]
    n = len(start)
    t = []
    for i in range(n):
        t.append((start[i],end[i]))

    print(t)


    print(activity_select(start, end,n))
    # print(selectActivity(t))
