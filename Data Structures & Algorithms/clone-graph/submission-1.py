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
        created = dict()
        created[node] = Node(node.val, [])
        queue = deque([node])
        while queue:
            curr = queue.popleft()
            for nxt in curr.neighbors:
                if nxt not in created:
                    created[nxt] = Node(nxt.val, [])
                    queue.append(nxt)

                created[curr].neighbors.append(created[nxt])
        return created[node]


