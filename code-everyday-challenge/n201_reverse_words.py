




def reverse_words(s):
    s_list = s.split('.')

    s_final = s_list[-1]
    for i in range(len(s_list)-2,-1,-1):
        s_final = s_final +'.' +s_list[i]
        # print(s_list[i])

    return s_final





if  __name__ == "__main__":
    s = "i.like.this.program.very.much"
    print(reverse_words(s))