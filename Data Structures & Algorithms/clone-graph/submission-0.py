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
            return None
        degrees = dict()
        node_ref = dict()
        dup_node_ref = dict()
        queue = [node]
        while queue:
            v = queue.pop(0)
            node_ref[v.val] = v
            dup_node_ref[v.val] = Node(v.val, [])
            for nv in v.neighbors:
                if nv.val not in node_ref:
                    queue.append(nv)
        for val, cnode in node_ref.items():
            dup_node_ref[val].neighbors = [dup_node_ref[cn.val] for cn in cnode.neighbors]
        return dup_node_ref[node.val]


