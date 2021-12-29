import sys
import collections
# 이진 트리 반전

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 1. 파이썬다운 방식 
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

    # 2. 반복구조로 BFS
    def invertTree2(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root]) # BFS -> 덱 사용

        while queue:
            node = queue.popleft() # 덱 -> popleft()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left # 왼쪽노드 오른쪽 노드 스왑

                queue.append(node.left)
                queue.append(node.right)

        return root

    def invertTree3(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root]) # DFS -> 스택 사용

        while stack:
            node = stack.pop() # 스택 -> pop()
            # 부모 노드 부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)

        return root