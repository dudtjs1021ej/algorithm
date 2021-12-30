# 이진탐색트리(BST)에서 자신과 같거나 큰 값을 가진 모든 노드의 합을 각 노드로 만들어라
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    val: int = 0 # 누적 값

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 자신 노드의 값과 루트의 우측에 있는 모든 노드의 값을 더하면 됨 -> 중위 순회 (오른쪽->루트->왼쪽)
        if root:
            self.bstToGst(root.right) # 오른쪽 노드 내려감
            self.val += root.val # 지금까지 누적 값
            root.val = self.val # 현재 노드 값
            self.bstToGst(root.left) # 왼쪽 노드 

        return root