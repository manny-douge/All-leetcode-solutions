#Given a sorted array nums, remove the duplicates in-place such that each element
#appears only once and returns the new length.
#
#Do not allocate extra space for another array, you must do this by modifying the
#input array in-place with O(1) extra memory.
#
#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4]
#Explanation: Your function should return length = 5, with the first five
#elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't
#matter what values are set beyond the returned length.
ans = 5
nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)


        #2 pointer pattern
        pointer_1 = 0
        pointer_2 = 1
        end = len(nums)-1

        while pointer_1 < end:
            if nums[pointer_1] == nums[pointer_2]:
                nums.pop(pointer_1)
                end -= 1
            else:
                pointer_1 += 1
                pointer_2 += 1


        return len(nums)

Solution().removeDuplicates(nums)
print(f"Input: {nums}, Correct_answer: {ans}")
print(f"Output: {nums}, My answer: {Solution().removeDuplicates(nums)}")

