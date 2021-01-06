#Say you have an array prices for which the ith element is the price of a given
#stock on day i.
#
#Design an algorithm to find the maximum profit. You may complete as many
#transactions as you like (i.e., buy one and sell one share of the stock multiple
#times).
#
#Note: You may not engage in multiple transactions at the same time (i.e., you
#must sell the stock before you buy again).
#

def maxProfit(prices):

    #define profit
    
    #going from low point to a high point
    #once we find this point profit is defined as
    #difference between high point - low point
    #how do we find profit? low -> point
    #what sthe value? profit = high_point - low point
    
    max_profit = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            profit = prices[i+1] - prices[i]
            max_profit += profit
    
    return max_profit


result = maxProfit([7,1,5,3,6,4])

print("Correct answer: 7")
print("Our answer: ", result)
