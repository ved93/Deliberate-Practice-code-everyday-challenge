

def get_nth_gp(a,r,N):

    if N == 1:
        return a

    return r*get_nth_gp(a,r,N-1) 

    


if __name__ == "__main__":
    a = 2
    r = 3
    N= 5
    print(get_nth_gp(a,r, N))