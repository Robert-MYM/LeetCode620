# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        #依旧是中序遍历，不同的是不需要记录整体，只需记录上一个，和出错的部分，在结束后调整
        self.n1=self.n2=self.prev=None
        self.inorder(root)
        self.n1.val,self.n2.val=self.n2.val,self.n1.val

    def inorder(self, root):
        if root.left != None: self.inorder(root.left)
        if self.prev and self.prev.val>root.val: #发现错误
            self.n2=root
            if self.n1==None:self.n1=self.prev
        self.prev=root
        if root.right != None: self.inorder(root.right)
        return