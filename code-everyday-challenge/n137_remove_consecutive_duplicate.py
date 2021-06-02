


def remove_duplicates(st):

    # prev = st[0]
    # st_new = prev
    # for i in st[1:]:
    #     if prev != i:
    #         st_new= st_new+i
    #     prev = i 

    # print(st_new)

    if len(st) <= 1:
        return st
    
    if st[0] ==st[1]:
        s = remove_duplicates(st[1:])
        return s
    else:
        s = remove_duplicates(st[1:])

        return st[0]+s






if __name__ == "__main__":
    st = 'geeksforgeeks'

    print(remove_duplicates(st))