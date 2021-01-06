#Write a function to delete a node in a singly-linked list. You will not be given
#access to the head of the list, instead you will be given access to the node to
#be deleted directly.
#
#It is guaranteed that the node to be deleted is not a tail node in the list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #4 -> 5 -> 1 -> 9
        #4 -> 1 -> 1 -> 9
        #copy value from next node to "deleted" node
        node.val = node.next.val

        #4 -> 1 -> 1 -> 9
        #4 -> 1 -> 1 -> 9
        #        |___|
        #set next pointer after "deleted" node
        node.next = node.next.next



