# 129. SUM ROOT TO LEAF NUMBERS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(cur, num):
            if not cur:
                return 0
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num
            left_sum = dfs(cur.left, num)
            right_sum = dfs(cur.right, num)
            return left_sum + right_sum
        
        return dfs(root, 0)
