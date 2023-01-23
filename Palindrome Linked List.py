# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        currunt = head 
        prev = head 
        while currunt and currunt.next :
            prev = prev.next
            currunt = currunt.next.next
        node = None
        while prev:
            nxt = prev.next
            prev.next = node
            node = prev
            prev = nxt
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
