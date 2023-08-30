'''
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

Constraints:
The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

Test Cases:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Input: root = []
Output: []
'''
# ITERATIVE BFS
from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        
        rootNode = TreeNode(root.val)
        q = deque([(rootNode, root)])
        while q:
            parent, curr = q.popleft()
            prev_bnode = head_bnode = None
            for child in curr.children:
                new_bnode = TreeNode(child.val)
                if prev_bnode:
                    prev_bnode.right = new_bnode
                else:
                    head_bnode = new_bnode
                prev_bnode = new_bnode
                q.append((new_bnode, child))

            parent.left = head_bnode

        return rootNode
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        rootNode = data
        if not rootNode:
            return None
        root = Node(rootNode.val, [])
        q = deque([(root, rootNode)])
        while q:
            parent, curr = q.popleft()

            sibling = curr.left
            while sibling:
                new_nnode = Node(sibling.val, [])
                parent.children.append(new_nnode)
                q.append((new_nnode, sibling))
                sibling = sibling.right

        return root           
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))


# RECURSIVE DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        root_node = TreeNode(root.val)
        if len(root.children) > 0:
            first_child = root.children[0]
            root_node.left = self.encode(first_child)
        
        curr = root_node.left

        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right
        
        return root_node

	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        root_node = Node(data.val, [])
        curr = data.left
        while curr:
            root_node.children.append(self.decode(curr))
            curr = curr.right
        
        return root_node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))