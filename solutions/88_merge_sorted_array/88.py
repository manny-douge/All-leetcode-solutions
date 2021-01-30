#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
#sorted array.
#
#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has a size equal to m + n such that it has enough
#space to hold additional elements from nums2.
#
# 
#
#Example 1:
#
#Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
answer = [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
 
    #copy the inuse elements into another array to simplify index management
    copy = []
    for index in range(m):
        copy.append(nums1[index])
    
  
    p1 = 0
    p2 = 0
    write = 0
    
    #iterate while p1 < m and p2 < n:
    while p1 < m and p2 < n:
        if copy[p1] < nums2[p2]:
            nums1[write] = copy[p1]
            p1 += 1
        else:
            nums1[write] = nums2[p2]
            p2 += 1
        #increment write
        write += 1
    
    #we have exhausted one of the lists
    if p1 < m:
        #funnel remaining elements into num1s
        for index in range(p1, m):
            nums1[write] = copy[index]
            write += 1
    
    if p2 < n:
        for index in range(p2, n):
            nums1[write] = nums2[index]
            write += 1
            
print(f"Input: nums1:{nums1} m:{m} nums2:{nums2} n:{n}") 
print(f"Correct answer: [1,2,2,3,5,6]")
merge(nums1, m, nums2, n)
print(f"My answer: {nums1}")
            
