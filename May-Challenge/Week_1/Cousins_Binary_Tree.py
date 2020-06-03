class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None or x == root.val or y == root.val:
            return False
        lst = [root]
        # print(lst)
        xp,yp=None,None
        while len(lst) > 0 and xp is None and yp is None:
            next_lst = []
            for node in lst:
                if node.left:
                    if node.left.val == x:
                        xp = node
                    elif node.left.val == y:
                        yp = node
                    next_lst.append(node.left)
                if node.right:
                    if node.right.val == x:
                        xp = node
                    elif node.right.val == y:
                        yp = node
                    next_lst.append(node.right)
            lst = next_lst
        if not xp or not yp:
            return False
        return xp != yp
