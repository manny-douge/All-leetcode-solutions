#Given head, the head of a linked list, determine if the linked list has a cycle
#in it.
#
#There is a cycle in a linked list if there is some node in the list that can be
#reached again by continuously following the next pointer. Internally, pos is
#used to denote the index of the node that tail's next pointer is connected to.
#Note that pos is not passed as a parameter.
#
#Return true if there is a cycle in the linked list. Otherwise, return false.
#
# 
#
#Example 1:
#
#
#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        
        slow_runner = head
        fast_runner = head.next
        
        #runn the track with fast and slow
        #when do we sstop?
        #when we see our budy again
        while slow_runner != fast_runner:
            #what happpens here?
            if fast_runner is None or fast_runner.next is None:
                return False
            
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            
            
        
        #if we make it out here?
        #what does it mean
        return True



