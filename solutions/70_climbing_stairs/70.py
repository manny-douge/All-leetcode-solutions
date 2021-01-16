#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you
#climb to the top?
#
# 
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
n = 3
correct_ans = 3

class Solution:
    def climb(self, i, n, memo):
        if i == n:
            return 1
        if i > n:
            return 0

        #magic sauz
        memo[i] = self.climb(i+1, n, memo) + self.climb(i+2, n, memo)
        return memo[i]


    def climbStairs(self, n):
        memo = {}
        return self.climb(0, n, memo)


print(f"Input: {n}, Correct_answer: {correct_ans}")
print(f"Correct Answer: {Solution().climbStairs(n)}")



