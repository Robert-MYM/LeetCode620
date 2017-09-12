# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:return True
        if abs(self.height(root.left)-self.height(root.right))<=1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False

    def height(self,root):
        if root==None:return 0
        return max(self.height(root.left),self.height(root.right))+1

