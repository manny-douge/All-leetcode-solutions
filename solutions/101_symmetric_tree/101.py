#Given a binary tree, check whether it is a mirror of itself (ie, symmetric
#around its center).
#
#For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
# 
#
#But the following [1,2,2,null,3,null,3] is not:
#
#    1
#   / \
#  2   2
#   \   \
#   3    3

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self, left, right):

        #handle when missing nones
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)



    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.isMirror(root.left, root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None,
None)), TreeNode(2, TreeNode(4, None, None), TreeNode(3, None,None)))
correct_answer = True
print(f"Input is the tree in the code, correct_answer:{correct_answer}")
print(f"My answer:{Solution().isSymmetric(root)}")
