 
# when you need all possible combinations
#https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm

def nested_fors(n,firstfor,x):
    store = []

    if firstfor < n:
        for x[firstfor] in ['a', 'b','c']:
            nested_fors(n,firstfor+1,x)
    else:
        print(x)



nested_fors(3,0,['']*3)