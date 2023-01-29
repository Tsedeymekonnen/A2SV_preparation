# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        result=[]
        while head:
            while stack and stack[-1][1] < head.val:
                result[stack.pop()[0]] = head.val
            stack.append([len(result), head.val]) 
            result.append(0)  
            head = head.next
        return result 
