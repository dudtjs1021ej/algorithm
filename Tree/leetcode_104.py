import collections
# 이진트리의 최대 깊이

# 트리노드
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root]) #데크 -> O(1) 로 양방향 모두 추출 가능
        depth = 0

        while queue:
            depth += 1
            # pop한 노드의 자식 노드 append
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수가 깊이
        return depth