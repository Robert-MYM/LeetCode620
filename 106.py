# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        l=len(postorder)
        if l== 0: return None
        val=postorder[l-1]
        Node=TreeNode(val)
        if l==1:return Node
        k=inorder.index(val)
        if k == 0:
            Node.left = None
        else:
            Node.left = self.buildTree(inorder[:k],postorder[:k])
        if k == len(inorder) - 1:
            Node.right = None
        else:
            Node.right = self.buildTree(inorder[k + 1:],postorder[k:l-1])
        return Node