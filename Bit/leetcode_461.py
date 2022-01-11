# 두 정수를 입력받아 몇 비트가 다른지 계산하라.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1') # bin으로 이진수 변환 -> XOR : 다르면 무조건 1이기때문에 1의개수 리턴