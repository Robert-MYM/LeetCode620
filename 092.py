# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy, diff = ListNode(0), n - m
        dummy.next = head
        prev, curr = dummy, dummy.next
        while m > 1:
            prev, curr = curr, curr.next
            m -= 1
        last_unswapped, first_swapped = prev, curr
        while curr and diff >= 0:
            curr.next, prev, curr = prev, curr, curr.next
            diff -= 1
        last_unswapped.next, first_swapped.next = prev, curr
        return dummy.next