# FLATTEN BINARY TREE TO LINKED LIST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None

            leftTrail = dfs(root.left)
            rightTrail = dfs(root.right)

            if root.left:
                leftTrail.right = root.right
                root.right = root.left
                root.left = None

            return rightTrail or leftTrail or root 

        dfs(root)

        