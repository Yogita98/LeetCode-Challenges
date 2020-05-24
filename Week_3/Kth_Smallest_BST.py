# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        left_node_arr = []
        node = root
        # kth_smallest=0
        while left_node_arr or node:
            if node:
                left_node_arr.append(node)
                node = node.left
            else:
                node = left_node_arr.pop()
                kth_smallest = node.val
                k -= 1
                if k==0:
                    break
                node = node.right
        return kth_smallest