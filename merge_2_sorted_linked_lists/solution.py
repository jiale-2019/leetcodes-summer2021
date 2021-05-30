# Source: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l3_end = ListNode()
        l3_start = ListNode(next = l3_end)
        
        
        while l1 != None or l2 != None:
            
            if l1 == None:
                l3_end.next = l2
                l2 = None
            
            elif l2 == None:
                l3_end.next = l1
                l1 = None
            
            elif l1.val > l2.val:
                l3_end.next = l2
                l3_end = l2
                l2 = l2.next
                
            else:
                l3_end.next = l1
                l3_end = l1
                l1 = l1.next
                
            
        return l3_start.next.next