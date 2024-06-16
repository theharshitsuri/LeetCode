# 105. CONSTRUCT A BINART TREE FROM PREORDER AND INORDER TRAVERSAL

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            # i = index for the root node
            i = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[i])
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
            return root
        