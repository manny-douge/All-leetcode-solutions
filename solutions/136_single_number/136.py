#Given a non-empty array of integers nums, every element appears twice except
#for one. Find that single one.
#
#Follow up: Could you implement a solution with a linear runtime complexity and
#without using extra memory?
#
# 
#
#Example 1:
#
#Input: nums = [2,2,1]
#Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        nums = sorted(nums)
        
        i = len(nums)-1
        
        while i != 0:
            first_num = nums[i]
            second_num = nums[i-1]
            if first_num == second_num:
                nums.pop(i)
                nums.pop(i-1)
                i = i - 2
            else:
                i = i - 1
        
            if len(nums) == 1:
                return nums[0]
        
                
