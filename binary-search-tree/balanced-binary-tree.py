'''
Given a binary tree, determine if it is height-balanced.

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

Testcases:
Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            
            height_left = dfs(root.left)
            height_right = dfs(root.right)

            # use -1 as a flag to indicate if the subtree is not balanced, real height will never be < 0
            is_balanced = abs(height_left - height_right) <= 1 and height_left != -1 and height_right != -1

            height = max(height_left, height_right) + 1 if is_balanced else -1
            
            return height
        
        height = dfs(root)
        return height != -1