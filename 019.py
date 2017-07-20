# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        header=ListNode(0)
        header.next=head #记录头
        p1=p2=header
        for i in range(n):p1=p1.next
        while p1.next:
            p1=p1.next
            p2=p2.next
        p2.next=p2.next.next
        return header.next