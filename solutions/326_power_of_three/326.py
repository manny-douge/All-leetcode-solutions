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

n = 27
answer = True

class Solution:
    def isPowerOfThree(self, n):
        if n == 0:
            return False

        curr = 0
        power = 0
        #while curr != n
        while curr != n:
            #calculate the curr for this power
            curr = 3 ** power
            #if curr is greater than n
            if curr > n:
                #return False, its not a power of three!
                return False
            power += 1
                
        #if we make it out here
        #then curr == n
        return True

print(f"Input: {n}, Answer: {answer}")
print(f"My answer: {Solution().isPowerOfThree(n)}")
