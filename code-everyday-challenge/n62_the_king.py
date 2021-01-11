
#https://www.geeksforgeeks.org/puzzle-maximum-number-kings-chessboard-without-check/
def main(l,w):
    l, w = max(l,w), min(w,l)
    result = 0
    count = 0
    
    mn=min(l // 3,w//3)
    count += mn*8
    bl = l%3
    if bl == 2:
        count += (w//3)*5
        count+=(w%3)*2-1
    if bl == 1:
        count += (w//3)*2

    bw = w%3
    if bw == 2:
        count += (l//3)*5
        count+=(l%3)*2-1
    if bw == 1:
        count += (l//3)*2
    
    print(count)







if __name__ == '__main__':

    print(main(9,3))