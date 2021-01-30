#Given a singly linked list, determine if it is a palindrome.
#
#Example 1:
#
#Input: 1->2
#Output: false
#Example 2:
#
#Input: 1->2->2->1
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        
        #we are going to create a stack
        stack = []
        
        temp = head
        #iterate through linked list
        while temp is not None:
            #add val to the stack
            stack.append(temp.val)
            temp = temp.next
        
        temp = head
        #iterate through linked list again
        while temp is not None:
            #if stack.pop != ll.val:
            if stack.pop() != temp.val:
                return False
                #return False , no pally here!
            temp = temp.next
                
        
        #if we make it outside of this for loop
        return True
        
n = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
answer = True

print(f"Input: [1, 2, 2, 1] Answer: {answer}")
print(f"My answer: {Solution().isPalindrome(n)}")
