#given two strings s and t check if s is substring of t. 
#https://www.coursera.org/learn/competitive-programming-core-skills/lecture/z9nnC/worst-cases

# https://www.coursera.org/learn/competitive-programming-core-skills/lecture/wSCUn/defining-solution-set



def main(s,t):

    j =0
    m=''
    for i in t:
        if (i ==s[j]) :
            j+=1
            m=m+i
        if j == len(s):
            break
    if m == s:
        return 'YES'
    else:
        return 'NO'

    # print(m)
        




    return 0

if __name__ == "__main__":
    s= "cabc"  #"abac"
    t = "abacabab"
    print(main(s,t)) 