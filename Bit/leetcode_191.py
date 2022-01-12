def hammingWeight(self, n: int) -> int:
    return bin(n).count(1) # n^0 에서 0생략