
def change_money(m):
    total =0
    if m < 5:
        return m 
    elif m >= 10:
        total = total + m//10
        return total +change_money(m%10)
    else:
        total = total +m // 5
        return total+change_money(m%5)







if __name__ == '__main__':
    m = int(input())
    print(change_money(m))


    