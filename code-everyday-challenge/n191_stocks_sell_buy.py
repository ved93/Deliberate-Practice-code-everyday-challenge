
# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1/?track=md-arrays&batchId=144


def max_profit(price, start, end):

    if end <=  start:
        return 0
    
    profit = 0

    for i in range(start, end,1):

        for j in range(i+1, end+1,1):
            if (price[j] > price[i]):
                
                # Update the current profit
                curr_profit = price[j] - price[i] +\
                            max_profit(price, start, i - 1)+ \
                            max_profit(price, j + 1, end)

                # Update the maximum profit so far
                profit = max(profit, curr_profit)

    return profit


def stockBuySell(price,n):

    if n == 1:
        return 0

    i = 0
    while i < n-1:


        while ((i < (n - 1)) and (price[i + 1] <= price[i])):
            i += 1

        if (i == n - 1):
            break
        
        # Store the index of minima
        buy = i
        i += 1

        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1
            
        # Store the index of maxima
        sell = i - 1
        
        print("Buy on day: ",buy,"\t",
                "Sell on day: ",sell)

        return (buy, sell)










if __name__ == '__main__':
    price = [100, 180, 260, 310, 40, 535, 695]
    n = len(price)

    # print(max_profit(price, 0, n - 1))
    print(stockBuySell(price, len(price)))
