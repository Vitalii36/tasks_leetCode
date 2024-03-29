'''
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two
trees are overlapped while the others are not. You need to merge the two trees
into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null node
will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.



Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]


Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solver(self, r1, r2):
        if r1 == None and r2 == None:
            return None
        if r1 and r2:
            root = TreeNode(r1.val + r2.val)
            root.left = self.solver(r1.left, r2.left)
            root.right = self.solver(r1.right, r2.right)
            return root
        elif r1 == None:
            return r2
        else:
            return r1

    def mergeTrees(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:

        return self.solver(root1, root2)