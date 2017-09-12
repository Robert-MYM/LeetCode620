# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #随便用一个遍历方法，同时遍历2颗树
        if p==None and q==None:return True
        elif p!=None and q==None:return False
        elif p==None and q!=None:return False
        else:
            if p.val!=q.val:return False
            if self.isSameTree(p.left,q.left)==False:return False
            if self.isSameTree(p.right, q.right) == False: return False
            return True

