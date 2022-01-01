from typing import List
# 전위순회, 중위순회 결과를 보고 이진트리를 구축하라.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
          
            index = inorder.index(preorder.pop(0)) # 전위 순위의 첫번째 값은 루트값

            # 전위 순회의 첫번째값을 기준으로 왼쪽노드 오른쪽 노드 나눔
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node