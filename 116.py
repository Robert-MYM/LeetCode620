# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    #BFS
    def connect(self, root):
        if root==None:return
        arr=[root]
        tmp=[]
        while arr:
            for node in arr:
                if node.right:tmp.append(node.right)
                if node.left:tmp.append(node.left)
            arr=tmp
            A=None
            while tmp:
                B=tmp.pop()
                B.next=A
                A=B





