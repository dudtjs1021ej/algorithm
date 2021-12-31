#이진탐색트리가 주어졌을 떄, L 이상 R 이하의 값을 지닌 노드의 합을 구하라

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #풀이3 - 반복 구조 DFS로 풀이
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop() # ( BFS는 stack.pop(0) )
            if node:
                if node.val > L: 
                    stack.append(node.left) # 조건에 맞는 노드 stack에 넣음
                if node.val < R:
                    stack.append(node.right)

                if L <= node.val <= R:
                    sum += node.val

                print(stack) 
                '''
                [TreeNode{val: 5, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, TreeNode{val: 15, left: None, right: TreeNode{val: 18, left: None, right: None}}]
                [TreeNode{val: 5, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, None]
                [TreeNode{val: 7, left: None, right: None}]
                [None]
                '''
        return sum