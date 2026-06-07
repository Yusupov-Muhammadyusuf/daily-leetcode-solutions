"""
LeetCode: Create Binary Tree From Descriptions
Level: Medium 🟡

Description:
Given a 2D integer array descriptions where descriptions[i] = [parent_i, child_i, isLeft_i] 
indicates that parent_i is the parent of child_i in a binary tree.
Construct the binary tree and return its root.

Example:
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]

Approach: Hash Map (Dictionary) + Set
1. We use a dictionary 'nodes' to store and reuse TreeNode instances by their values.
2. We iterate through the descriptions to build the parent-child connections.
3. We keep track of all child nodes in a 'children' set.
4. The root of the tree will be the only node value that is a parent but never appears as a child.

Time Complexity: O(n) - We iterate through the descriptions list and node keys a constant number of times.
Space Complexity: O(n) - We store up to 'n' unique nodes in the hash map and children set.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 'nodes' dictionary ensures only one TreeNode instance is created per unique value
        nodes = {}
        # 'children' set tracks all nodes that have a parent
        children = set()

        for parent, child, isLeft in descriptions:
            # If parent node doesn't exist yet, create it
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            # If child node doesn't exist yet, create it
            if child not in nodes:
                nodes[child] = TreeNode(child)
            
            # Add child to the set (needed to find the root later)
            children.add(child)
            
            # Establish the link based on isLeft flag
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
        # Find the actual root of the tree.
        # The root node will never appear in the children set.
        for parent in nodes:
            if parent not in children:
                return nodes[parent] # Return the root as soon as it's found
