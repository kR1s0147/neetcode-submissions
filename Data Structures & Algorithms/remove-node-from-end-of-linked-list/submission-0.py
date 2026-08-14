# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l =0 
        start = head 
        while start:
            l=l+1
            start = start.next
        l = l-n

        dum=start= ListNode(0,head)
        
        while l>0:
            dum = dum.next
            l = l-1
        dum.next = dum.next.next
        return start.next