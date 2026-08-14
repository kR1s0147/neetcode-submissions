# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        if not l1:
            return l2
        elif not l2:
            return l1
        newhead = curr = ListNode()

        while l1 and l2:
            add = l1.val + l2.val+carry
            l1 = l1.next
            l2 = l2.next
            digit = add % 10
            if add // 10 > 0 :
                carry = add // 10
            else:
                carry = 0
            n = ListNode(digit)
            curr.next = n
            curr = n
        
        while l1:
            add = l1.val + carry
            l1 = l1.next
            digit = add % 10
            if add // 10 > 0 :
                carry = add // 10
            else:
                carry = 0
            n = ListNode(digit)
            curr.next = n
            curr = n

        while l2:
            add = l2.val + carry
            l2 = l2.next
            digit = add % 10
            if add // 10 > 0 :
                carry = add // 10
            else:
                carry = 0
            n = ListNode(digit)
            curr.next = n
            curr = n

        if (not l1) and (not l2) and (carry > 0):
            curr.next = ListNode(carry)
        return newhead.next

        