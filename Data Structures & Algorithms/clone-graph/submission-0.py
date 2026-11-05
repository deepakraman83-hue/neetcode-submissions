"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        start=node
        visited=set()
        stack=[start]
        visited.add(start)
        o_t_n={}
        while stack:
            node=stack.pop()
            o_t_n[node]=Node(val=node.val)
            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        
        for old_node,new_node in o_t_n.items():
            for nei in old_node.neighbors:
                new_nei=o_t_n[nei]
                new_node.neighbors.append(new_nei)

        return o_t_n[start]
