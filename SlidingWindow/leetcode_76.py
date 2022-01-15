import collections
# 문자열 s, t 를 입력받아 t의 모든 문자가 포함된 s의 최소 윈도우를 찾아라.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t) # 필요한 문자의 각자 개수
        missing = len(t) # 필요한 문자 전체 개수
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0 # 현재 문자가 필요한 문자라면
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                while left < right and need[s[left]] < 0: # 필요한 문자 수보다 더 제거 되었으면? -> 음수
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]