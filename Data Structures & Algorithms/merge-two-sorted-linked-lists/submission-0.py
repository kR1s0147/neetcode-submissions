# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2 = list1,list2

        if not list1:
            return list2
        elif not list2:
            return list1
        dummy = node = ListNode()
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                node.next = curr1
                node = curr1
                curr1 = curr1.next
                
            elif curr1.val > curr2.val:
               node.next = curr2
               node = curr2
               curr2 = curr2.next
        node.next = curr1 or curr2

        return dummy.next
            