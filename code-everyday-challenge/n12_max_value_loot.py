
import sys

def get_optimal_value(capacity,weights,values):
    total =0
    store= dict(zip(values,weights))
    print(store)
    wt=store[max(values)]
    # for i in weights
    if wt< capacity:
        capacity = capacity-wt   
        values.remove(max(values))
        weights.remove(wt)
        get_optimal_value(capacity, weights,values)
    else:









if __name__ == "__main__":    
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[:2]
    # print(data)
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    # print(values)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

