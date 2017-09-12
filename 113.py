# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res=[]
        self.dfs(root,sum,[])

    def dfs(self,root,sum,rec):
        rec.append(root.val)
        if root.val==sum and root.left==None and root.right==None:
            self.res.append(rec[:])
        else:
            if root.left!=None:
                self.dfs(root.left,sum-root.val,rec)
            if root.right!=None:
                self.dfs(root.right,sum-root.val,rec)
        rec.pop()
