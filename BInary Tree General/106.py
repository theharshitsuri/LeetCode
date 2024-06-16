# 106. CONSTRUCT BINARY TREE FROM INORDER AND POSTORDER TRAVERSAL

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            i = inorder.index(postorder.pop(-1))
            root = TreeNode(inorder[i])
            root.right = self.buildTree(inorder[i+1:], postorder)
            root.left = self.buildTree(inorder[:i], postorder)
            return root
        