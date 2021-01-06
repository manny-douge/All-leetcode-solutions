#Given an array nums of size n, return the majority element.
#
#The majority element is the element that appears more than ⌊n / 2⌋ times. You
#may assume that the majority element always exists in the array.
#
# 
#
#Example 1:
#
#Input: nums = [3,2,3]
#Output: 3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        #sliding window pattern
        #[3, 2, 1, 5 , 7, 4,4,4]

        #[1,2, 3, 4, 4, 5 , 7,7,7,7]

        nums = sorted(nums)

        outer = 0
        while outer < len(nums):
            current_num = nums[outer]
            total_for_num = 0
            inner = outer
            while inner < len(nums):
                if current_num == nums[inner]:
                    total_for_num = total_for_num + 1
                    if total_for_num > len(nums)/2:
                        return current_num
                    inner = inner + 1
                else:
                    outer = inner - 1
                    break
            outer = outer + 1

            
