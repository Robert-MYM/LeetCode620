# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #被绕的头都大了，其实画图就能秒解
        if not head:return
        if not head.next:return head
        dummy=ListNode(0)
        dummy.next=head
        p1=dummy
        p2=head
        while p2 and p2.next:
            p1.next=p2.next        #0-->2
            p2.next=p1.next.next   #1-->3
            p1.next.next=p2        #2-->1
            p1=p2
            p2=p2.next
        return dummy.next
