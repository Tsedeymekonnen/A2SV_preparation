# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        while head != None:
           nums.append(head.val)
           head = head.next
        nums = sorted(nums)   
        m = ListNode(0)
        res = m 
        for i in nums :
            m.next = ListNode(i)
            m = m.next
        return res.next 
