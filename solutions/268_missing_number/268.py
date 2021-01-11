#Given an array nums containing n distinct numbers in the range [0, n], return
#the only number in the range that is missing from the array.
#
#Follow up: Could you implement a solution using only O(1) extra space complexity
#and O(n) runtime complexity?
#
# 
#
#Example 1:
#
#Input: nums = [3,0,1] Output: 2 Explanation: n = 3 since there are 3 numbers, so
#all numbers are in the range [0,3]. 2 is the missing number in the range since
#it does not appear in nums.  Example 2:
#
#Input: nums = [0,1] Output: 2 Explanation: n = 2 since there are 2 numbers, so
#all numbers are in the range [0,2]. 2 is the missing number in the range since
#it does not appear in nums.  Example 3:
#
#Input: 
nums = [9,6,4,2,3,5,7,0,1]
output = 8

#Time Complexity = O(n)
#Space Complexity = O(1)

class Solution:
    def missingNumber(nums):
        num_len = len(nums)
        correct_sum = (num_len*(num_len+1))/2

        for num in nums:
            correct_sum -= num

        return int(correct_sum)

print(f"Input: {nums}, correct answer: {output}")
print(f"My answer: {Solution.missingNumber(nums)}")
