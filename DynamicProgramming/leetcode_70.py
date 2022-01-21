import collections
# 1계단 또는 2계단으로만 오를 때 오를 수 있는 방법 수
#-> 피보나치 수열과 유사

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]