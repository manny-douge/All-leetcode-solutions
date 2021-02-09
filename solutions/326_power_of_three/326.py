#Given an integer n, return true if it is a power of three. Otherwise, return
#false.
#
#An integer n is a power of three, if there exists an integer x such that n == 3x.
#
# 
#
#Example 1:
#
#Input: n = 27
#Output: true
#Example 2:
#
#Input: n = 0
#Output: false
import math

n = 27
answer = True

class Solution:
    def isPowerOfThree(self, n):
        if n == 0:
            return False

        low = 0
        high = n
        #while curr != n
        while low < high:
            mid = low + math.floor((high-low)/2);
            if 3 ** mid == n:
                return True 
            elif 3 ** mid > n:
                high = mid
            elif 3 ** mid < n:
                low = mid + 1

        return False 

print(f"Input: {n}, Answer: {answer}")
print(f"My answer: {Solution().isPowerOfThree(n)}")
