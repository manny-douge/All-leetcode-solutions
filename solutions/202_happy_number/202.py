#Write an algorithm to determine if a number n is happy.
#
#A happy number is a number defined by the following process:
#
#Starting with any positive integer, replace the number by the sum of the squares
#of its digits.  Repeat the process until the number equals 1 (where it will
#stay), or it loops endlessly in a cycle which does not include 1.  Those numbers
#for which this process ends in 1 are happy.  Return true if n is a happy number,
#and false if not.
#
#Example 1:
#
#Input: n = 19
#Output: true
#Explanation:
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1
#
#Example 2:
#
#Input: n = 2
#Output: false

n = 19
correct_ans = True

class Solution:
    def isHappy(n):
        
        #keep dictionary
        seen = {}
        
        while n != 1:
            sum = 0
            #linear summate squares
            for _ in range(len(str(n))):
                num = n % 10
                n = int(n / 10)
                sum += num ** 2
                #update n with sum
            n = sum
            if sum in seen:
                #were in a loop get me out
                return False
            else:
                seen[sum] = 1


        return True

print(f"Input: {n}, Correct Answer:{correct_ans}")
print(f"My answer: {Solution.isHappy(n)}")
