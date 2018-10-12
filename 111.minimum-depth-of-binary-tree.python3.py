#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (34.05%)
# Total Accepted:    244.7K
# Total Submissions: 716.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        queue = []
        queue.append(root)
        level = 1
        while queue:
            cur_level = len(queue)
            while cur_level:
                temp = queue.pop(0)
                if self.isLeaf(temp):
                    return level
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                cur_level -= 1
            level += 1


    
    def isLeaf(self, node):
        return not ( node.left or node.right)
