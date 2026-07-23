from collections import deque
from typing import Optional

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"
        self.res = [str(root.val)]
        self.bfs(root)
        return ','.join(self.res)

    def bfs(self, root: Optional[TreeNode]) -> None:
        q = deque()
        q.append(root)
        while q:
            temp = q.popleft()
            for child in (temp.left, temp.right):
                if child:
                    q.append(child)
                    self.res.append(str(child.val))
                else:
                    self.res.append("null")

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "null":
            return None
        
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        
        while q and i < len(nodes):
            curr = q.popleft()

            # Left child
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1

            # Right child
            if i < len(nodes) and nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1

        return root
