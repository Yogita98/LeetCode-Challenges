# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def construct(root,val):
            if root:
                if val>root.val:
                    if root.right:
                        construct(root.right,val)
                    else:
                        root.right=TreeNode(val)
                else:
                    if root.left:
                        construct(root.left,val)
                    else:
                        root.left=TreeNode(val)
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            construct(root,preorder[i])
        return root
        