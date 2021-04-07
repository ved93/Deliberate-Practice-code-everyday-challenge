



def permute(n, firstfor,x,st = []):
    # store = []
    global store
    
    if firstfor < n:

        for x[firstfor] in ['0','1']:

            # store+=
            p=permute(n,firstfor+1,x,st)
            # return p
            # store.append(p)
            # if p :
            #     print(p)

            # print(p)

    else:
        # print(x)

        # nonlocal store
        # store.append(x)
        # print(st, '    ',x)
        x= ''.join(x)
        st.append(x)
        
        return x
        # store[]

    return st



if __name__ == "__main__":
    store = []
    print(permute(3,0,['']*3))
    # print(store)

# below is different . FOR DUPLICATE
#https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm