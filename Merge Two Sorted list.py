# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        res = result 
        if list1 == None and list2 == None :
            return result.next
        if list1 == None:
            return list2
        if list2 == None :
            return list1 
        if list1.val <= list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
        ref = result
        while list1 != None and list2 != None:
            if list1.val<= list2.val:
                ref.next = list1
                ref = ref.next
                list1 = list1.next
            else :
                ref.next = list2
                ref = ref.next
                list2 = list2.next  
        if list1 == None :
                ref.next = list2
        else:
                ref.next  = list1
        return result
