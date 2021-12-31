import sys
# 두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 루트의 왼쪽 자식 중 젤 차이가 없는 노드 = 왼쪽노드에서 제일 오른쪽에 있는 노드 / 오른쪽 자식에선 오른쪽 노드에서 제일 왼쪽에 있는 노드
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        # 반복 구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return result