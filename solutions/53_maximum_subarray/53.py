#Given an integer array nums, find the contiguous subarray (containing at least
#one number) which has the largest sum and return its sum.
#
# 
#
#Example 1:
#
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
import math
nums = [-2,1,-3,4,-1,2,1,-5,4]
correct_answer =  6

class Solution:
    def maxSubArray(self, nums):
        
        max_sum = -math.inf
        window_start = 0
        window_sum = 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            
            if window_sum > max_sum:
                max_sum = window_sum
                
            while window_sum < 0:
                window_sum -= nums[window_start]
                window_start += 1
        
        return max_sum

print(f"Input: {nums} Correct_answer: {correct_answer}")
print(f"My answer: {Solution().maxSubArray(nums)}")
