#Merge two sorted linked lists and return it as a sorted list. The list should be
#made by splicing together the nodes of the first two lists.
#
# 
#
#
#Input: l1 = [1,2,4], l2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#Example 2:
#
#Input: l1 = [], l2 = []
#Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        prev = ListNode()
        head = prev

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                prev.next  = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return head.next

list_1 = ListNode(1, ListNode(2, ListNode(4, None)))
list_2 = ListNode(1, ListNode(3, ListNode(4, None)))

sol = Solution().mergeTwoLists(list_1, list_2)
ans = list_2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4,
ListNode(4, None))))))

while sol is not None and ans is not None: 
    if sol.val == ans.val:
        print(f"Sol: {sol.val} == Ans: {ans.val}, good.")
    else:
        print(f"Fail:{sol.val} does not equal {ans.val}")
        exit() 
    sol = sol.next
    ans = ans.next

print("Pass.")
