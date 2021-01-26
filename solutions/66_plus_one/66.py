#Given a non-empty array of decimal digits representing a non-negative
#integer,increment one to the integer.
#
#The digits are stored such that the most significant digit is at the head of the
#list, and each element in the array contains a single digit.
#
#You may assume the integer does not contain any leading zero, except the number
#0 itself.
#
# 
#
#Example 1:
#
#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
fn_input = [9,9,9,9]
answer = [1,0,0,0,0]

class Solution:
    def plusOne(self, digits):


        index = len(digits)-1
        #loop over digits (reverse)
        while index >= 0:
            #if we see a 9
            if digits[index] == 9:
                #turn it to 0
                digits[index] = 0

            #else (its a non nine number)
            else:
                #add 1 to it
                digits[index] = digits[index] + 1
                #and return it
                return digits
            index -= 1

        #we made it while loopwhat does that mean?
        #it means that our input after transforming all 9's to 0s
        #is all zeroes
        digits.insert(0, 1)
        return digits
print(f"Input: {fn_input}, Correct Answer: {answer}")
print(f"My answer: {Solution().plusOne(fn_input)}")
