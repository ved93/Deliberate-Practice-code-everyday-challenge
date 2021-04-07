
def reverse_string(s):

    if len(s) <=1:
        return s

    return s[-1]+reverse_string(s[:-1])



if __name__ == "__main__":
    s='abhishek'
    # s = list(s)
    # print(s[0])
    print(reverse_string(s))