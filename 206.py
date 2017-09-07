# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:return head
        new_head=None
        while head!=None:
            p=head
            head=head.next
            p.next=new_head
            new_head=p
        return new_head