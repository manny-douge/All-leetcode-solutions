#Given an array nums, write a function to move all 0's to the end of it while
#maintaining the relative order of the non-zero elements.
#
#Example:
#
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Note:
#
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #[1, 12, 9, 0, 0, 6]
        #        [   ]
        windowStart = 0
        windowEnd = 0

        while windowEnd < len(nums):
            if nums[windowEnd] != 0:
                temp = nums[windowEnd]
                nums[windowEnd] = nums[windowStart]
                nums[windowStart] = temp

                windowStart = windowStart + 1

            windowEnd = windowEnd +1

        return nums
