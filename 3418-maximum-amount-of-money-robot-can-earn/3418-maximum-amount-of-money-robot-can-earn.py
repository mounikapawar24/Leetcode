from typing import List
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = float('-inf')

        # dp[j][k] -> current row
        dp = [[NEG_INF] * 3 for _ in range(n)]

        # initialize (0,0)
        val = coins[0][0]
        dp[0][0] = val
        if val < 0:
            dp[0][1] = 0  # neutralize first robber

        # first row
        for j in range(1, n):
            val = coins[0][j]
            new = [NEG_INF] * 3

            for k in range(3):
                if dp[j-1][k] == NEG_INF:
                    continue

                # don't neutralize
                new[k] = max(new[k], dp[j-1][k] + val)

                # neutralize if robber
                if val < 0 and k < 2:
                    new[k+1] = max(new[k+1], dp[j-1][k])

            dp[j] = new

        # remaining rows
        for i in range(1, m):
            new_dp = [[NEG_INF]*3 for _ in range(n)]

            for j in range(n):
                val = coins[i][j]

                for k in range(3):
                    best_prev = NEG_INF

                    # from top
                    best_prev = max(best_prev, dp[j][k])

                    # from left
                    if j > 0:
                        best_prev = max(best_prev, new_dp[j-1][k])

                    if best_prev == NEG_INF:
                        continue

                    # don't neutralize
                    new_dp[j][k] = max(
                        new_dp[j][k],
                        best_prev + val
                    )

                    # neutralize robber
                    if val < 0 and k < 2:
                        new_dp[j][k+1] = max(
                            new_dp[j][k+1],
                            best_prev
                        )

            dp = new_dp

        # answer = best with ≤2 neutralizations
        return max(dp[n-1])