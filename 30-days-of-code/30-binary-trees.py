from collections import deque


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def post_order(self, root):
        if root is not None:
            self.in_order(root.left)
            self.in_order(root.right)
            print(root.data)

    def pre_order(self, root):
        if root is not None:
            print(root.data)
            self.in_order(root.left)
            self.in_order(root.right)

    def level_order(self, root):
        q = deque()
        if root is not None:
            q.append(root)
        while len(q):
            tree = q.popleft()
            print(tree.data)
            if tree.left is not None:
                q.append(tree.left)
            if tree.right is not None:
                q.append(tree.right)

    levelOrder = level_order


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
# myTree.in_order(root)
# myTree.post_order(root)
# myTree.pre_order(root)
