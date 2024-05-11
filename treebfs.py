from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return
    queue = deque([root])
    visited = set()

    while queue:
        nodeobj = queue.popleft()
        if not nodeobj in visited:
            visited.add(nodeobj)
            print(nodeobj.val)
            for child in [nodeobj.left,nodeobj.right]:
                if child:
                    queue.extend([child])


# 示例树构建和DFS使用
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

bfs(node1)  # 输出: 1, 2, 4, 5, 3, 6