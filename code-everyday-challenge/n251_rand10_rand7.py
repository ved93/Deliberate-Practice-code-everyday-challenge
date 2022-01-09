
# https://leetcode.com/problems/implement-rand10-using-rand7/discuss/816927/Python-generalised-solution-for-RandM()-using-RandN()

def rand10():
    index =  41
    while index > 40:
        index = (rand7()-1) * 7 + rand7() 

    return (index -1) % 10 +1





if __name__ == "__main__":
    print(rand10(2))