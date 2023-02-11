#!/bin/python3

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow = head
    fast = head
    
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return 1
    
    return 0
if __name__ == '__main__':
