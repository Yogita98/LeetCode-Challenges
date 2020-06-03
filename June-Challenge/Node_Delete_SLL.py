# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val  # The node which has to be deleted is given as 'node'. To delete this node, we                                   # need prev node which is not givenhemce why we will copy the next node's value                                   # in the current node and make the current node point the next to next node which                                 # removes the next node out of the linked list.
        node.next=node.next.next
