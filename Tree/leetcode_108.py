import sys
from typing import List
# 정렬된 배열 -> 높이 균형 이진 탐색 트리로 변환
# 높이 균형 = 모든 노드의 두 서브 트리간 깊이 차이가 1 이하

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2 # 내림값 리턴 

        
        node = TreeNode(nums[mid])
        # 재귀 호출로 mid으로 반씩 나누면서 처리
        node.left = self.sortedArrayToBST(nums[:mid]) 
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

