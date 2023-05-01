'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSuccessor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def findPredecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                root = None
            elif root.right:
                root.val = self.findSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.findPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
        
        
            
            
        
                
            
            