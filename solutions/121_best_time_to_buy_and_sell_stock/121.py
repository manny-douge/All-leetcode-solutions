#You are given an array prices for which prices[i] is the price of a given stock
#on the ith day.
#
#You are only permitted to complete at most one transaction. In other words, you
#can buy one and sell one share of the stock. You cannot sell a stock before you
#buy one.
#
#Return the maximum profit you can achieve from this transaction. If you cannot
#achieve any profit, return 0.
#
# 
#
#Example 1:
#
#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#The answer is not 7-1 = 6, as selling price needs to be larger than buying price.
#Example 2:
#
#Input: prices = [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transactions are done and the max profit = 0.
# 

prices = [7,1,5,3,6,4]
correct_answer = 5
class Solution:
    def maxProfit(prices):
        max_profit = 0
        stock_price = 0
        index = 0
        
        while index < len(prices)-1:
            stock_price = prices[index]
            if stock_price < prices[index+1]:
                for inner in range(index, len(prices)):
                    if stock_price <= prices[inner]:
                        max_profit = max(max_profit, prices[inner]-stock_price)
                    else:
                        index = inner-1
                        break
            index += 1
        
        return max_profit

print(f"Input {prices}, correct_answer: {correct_answer}")
print(f"My answer: {Solution.maxProfit(prices)}")
