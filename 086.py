# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None or x is None:
            return head
        p1 = head1 = ListNode(0)
        p2 = head2 = ListNode(0)
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = head2.next
        p2.next = None
        return head1.next



