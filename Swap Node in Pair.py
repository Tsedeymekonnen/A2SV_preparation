# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        num1 = ListNode(0)
        num1.next = head 
        curr = num1 
        while curr.next != None and curr.next.next != None:
            frst = curr.next 
            sec = curr.next.next
            frst.next = sec.next 
            curr.next = sec 
            curr.next.next = frst 
            curr = curr.next.next 
        return num1.next
