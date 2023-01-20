# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        m1 = m2 = head
        
        le = 0
        
        while head:
            le += 1
            head=head.next
        
        head = m1
        
        if n == le:
            head = head.next
            return head
        
        target_length = 1
        
        while target_length < (le-n):
            target_length += 1
            head = head.next
            
        
        if head:
            head.next = head.next.next
        
        return m1
