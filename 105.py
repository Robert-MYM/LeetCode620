# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0: return None
        val = preorder[0]
        Node = TreeNode(val)
        if len(preorder) == 1: return Node
        k = inorder.index(val)
        if k == 0:
            Node.left = None
        else:
            Node.left = self.buildTree(preorder[1:len(inorder[:k]) + 1], inorder[:k])
        if k == len(inorder) - 1:
            Node.right = None
        else:
            Node.right = self.buildTree(preorder[len(inorder[:k]) + 1:], inorder[k + 1:])
        return Node


