# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
                        # invert the binary tree by recursively calling the fuction on leaf nodes to the root.
        return root
            
# Reference: https://www.youtube.com/watch?v=_i0jqdVkObU