# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev1 = ListNode(0)
        curr = head 
        while curr :
            prev = prev1 
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            next = curr.next 
            curr.next = prev.next
            prev.next = curr
            curr = next
        return prev1.next
