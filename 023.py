# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #和之前merge组合一下用
        ls=len(lists)
        if ls==0:return ListNode(0)
        if ls == 1: return lists[0]
        res=lists[0]
        i=1
        while i<ls:
            res=self.mergeTwoLists(res,lists[i])
            i+=1

        return res

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode(0)
        res=head
        while l1 and l2:
            if l1.val<=l2.val:
                res.next=l1
                l1=l1.next
            else:
                res.next=l2
                l2=l2.next
            res=res.next
        res.next=l1 or l2
        return head.next