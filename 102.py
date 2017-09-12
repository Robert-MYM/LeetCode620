# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #BFS
        res=[]
        if root==None:return res
        level=[root]
        while len(level)!=0:
            res.append([node.val for node in level])
            new_level=[]
            for node in level:
                if node.left:new_level.append(node.left)
                if node.right:new_level.append(node.right)
            level=new_level
        return res



