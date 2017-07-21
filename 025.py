# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:return
        if k==1:return head
        dummy = ListNode(0)
        dummy.next = head
        start=dummy
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if not end.next:return dummy.next
            (start.next,start)=self.reverse(start,end)
        return dummy.next

    def reverse(self,start,end):
        dummy=ListNode(0)
        dummy.next=start
        while dummy.next!=end:#reverse list 核心部分  loop1                   loop2         ...
            tmp=start.next                           #tmp=2--3--4             tmp=3-4
            start.next=tmp.next                      #start:1--3--4           start 1-4
            tmp.next=dummy.next                      #2--1--3--4              tmp3-2-1-4
            dummy.next=tmp                           #dummy：0-2-1-3-4          dummy0-3-2-1-4
        return (end,start)