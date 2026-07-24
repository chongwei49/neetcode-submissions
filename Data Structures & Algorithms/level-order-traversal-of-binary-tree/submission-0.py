# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def rec(root, level):
            nonlocal result
            if not root:
                return
            
            if level >= len(result):
                result.append([])

            result[level].append(root.val)

            rec(root.left, level+1)
            rec(root.right, level+1)

        rec(root, 0)
        return result
