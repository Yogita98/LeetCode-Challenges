# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or head.next==None:
            return head
        
        odd_pointer,even_pointer,even=head,head.next,head.next
        
        while even_pointer!=None and even_pointer.next!=None:
            odd_pointer.next=odd_pointer.next.next
            odd_pointer=odd_pointer.next
            even_pointer.next=even_pointer.next.next
            even_pointer=even_pointer.next
        
        odd_pointer.next=even
        
        return head
            