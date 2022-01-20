import collections
# 피보나치수

class Solution:
    dp = collections.defaultdict(int)

    # 하향식 풀이 -> 재귀
    def fib1(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]

    # 상향식 풀이 -> 반복
    def fib2(self, N: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]