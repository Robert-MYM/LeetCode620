# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head: return head
        if not head.next: return head
        if k == 0: return head
        count = 1
        tmp = head
        while tmp.next: tmp = tmp.next;count += 1  #先遍历一次链表，知道长度后对于k做优化，此处可以直接用数组的方式储存链表，之后一步到位，但感觉是邪教就没写
        kk = k % count
        for i in range(kk):
            tmp1 = tmp2 = head
            while tmp1.next:
                tmp2 = tmp1
                tmp1 = tmp1.next
            tmp1.next = head
            head = tmp1
            tmp2.next = None
        return head