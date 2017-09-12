# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #BST中序之后为升序数列，针对该特性进行判断，O(n)
        if root==None:return True
        self.res=[]
        self.inorder(root)
        for i in range(1,len(self.res)):
            if self.res[i-1]>=self.res[i]:return False
        return True

    def inorder(self,root):
        if root.left!=None:self.inorder(root.left)
        self.res.append(root.val)
        if root.right!=None:self.inorder(root.right)
        return
