
import sys

def get_optimal_value(capacity,weights,values):
    # total =0
    # store= dict(zip(values,weights))
    # print(store)
    # wt=store[max(values)]
    # # for i in weights
    # if wt< capacity:
    #     capacity = capacity-wt   
    #     values.remove(max(values))
    #     weights.remove(wt)
    #     get_optimal_value(capacity, weights,values)
    # else:
    value = 0
    res = {ind: i/j for ind,(i,j) in enumerate(zip(values,weights))}  
    #sort on the basis of values
    bst_ind =sorted(res, key = res.get, reverse =True)
    print(res, ' ', bst_ind)
    for i,j in enumerate(bst_ind):
        if capacity ==0:
            break

        amt = min(weights[j], capacity)
        value = value + amt*(values[j]/weights[j])
        capacity -= amt

    return value












if __name__ == "__main__":    
    # data = list(map(int, sys.stdin.read().split()))
    # n, capacity = data[:2]
    n,capacity = 3,50
    # print(data)
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    values =  [60,100,120]
    weights = [20,50,30]


    print(values, ' ', weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

