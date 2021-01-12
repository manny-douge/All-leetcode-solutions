#Given two arrays, write a function to compute their intersection.
#
#Example 1:
#
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#
#Note:
#
#Each element in the result should appear as many times as it shows in both
#arrays.
#The result can be in any order.
#Follow up:
#
#Q1. What if the given array is already sorted? How would you optimize your
#algorithm?  
#
#Q2. What if nums1's size is small compared to nums2's size? Which
#algorithm is better?  
#
#Q3. What if elements of nums2 are stored on disk, and the
#memory is limited such that you cannot load all elements into the memory at
#once?
from collections import defaultdict

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
correct_ans =  [4,9]
class Solution:
    def intersect(nums1, nums2):
        num1_dict = defaultdict(int)

        for num in nums1:
            if num in num1_dict:
                num1_dict[num] = num1_dict[num]+1
            else:
                num1_dict[num] = 1

        ans = []
        for num in nums2:
            if num in num1_dict and num1_dict[num] > 0:
                ans.append(num)
                num1_dict[num] = num1_dict[num]-1


        return ans
            
#Time complexity: O(m + n) where m is the length of nums1 and n is the length nums2
#Space complexity: O(n) where n is the length of nums1, but we could make this better
# by storing values in the dictionary of the smallest list.

print(f"nums1: {nums1},\nnum2: {nums2}\nCorrect Answer: {correct_ans}")
print(f"My answer: {Solution.intersect(nums1, nums2)}")
