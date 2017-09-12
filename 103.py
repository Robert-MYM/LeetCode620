# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None: return res
        k = 0
        level = [root]
        while len(level) != 0:
            if k % 2 == 0:
                res.append([node.val for node in level])
            else:
                a = [node.val for node in level]
                a.reverse()
                res.append(a)
            new_level = []
            for node in level:
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            level = new_level
            k += 1
        return res
