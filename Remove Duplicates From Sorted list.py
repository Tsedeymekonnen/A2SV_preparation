# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head != None): 
           prev = head
           curr = head.next
           while prev != None and curr != None:
              if prev.val == curr.val:
                 prev.next = curr.next
              else:
                 prev = prev.next
              curr= curr.next     
        return head         
       
