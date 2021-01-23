#Given the root of a binary tree, return its maximum depth.

#A binary tree's maximum depth is the number of nodes along the longest path from
#the root node down to the farthest leaf node.

 

#Example 1:


#Input: root = [3,9,20,null,null,15,7]
#Output: 3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None,
None), TreeNode(7, None,None)))
correct = 3

class Solution:
    def countDepth(self, node):
        if node is None:
            return 0
        return max(1+ self.countDepth(node.left), 1 + self.countDepth(node.right))
    def maxDepth(self, root):
        return self.countDepth(root)


print(f"root: [3,9,20,null,null,15,7], correct_answer: {correct}")
print(f"My answer: {Solution().maxDepth(root)}")
