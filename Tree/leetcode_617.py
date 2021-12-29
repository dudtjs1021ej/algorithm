import collections
# 두 이진 트리 병합
# 두 트리의 값을 더함
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 재귀 탐색
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2: # 왼쪽노드, 오른쪽노드 둘 다 존재할때만
            node = TreeNode(t1.val + t2.val)
            # print(node) # 3,4,5 만 프린트
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2