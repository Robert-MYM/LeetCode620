# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n=[]
        while head!=None:
            n.append(head.val)
            head=head.next
        return self.sortedArrayToBST(n)


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        k=len(nums)
        if k==0:return None
        if k==1:return TreeNode(nums[0])
        q=k/2
        Node=TreeNode(nums[q])
        if q==0:Node.left=None
        else:Node.left=self.sortedArrayToBST(nums[0:q])
        if q==k-1:Node.right=None
        else:Node.right=self.sortedArrayToBST(nums[q+1:])
        return Node