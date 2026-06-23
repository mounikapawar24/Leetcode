class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # up[v]: arrays ending at value v whose last step was increasing
        # down[v]: arrays ending at value v whose last step was decreasing
        up = [0] * m
        down = [0] * m

        # length = 2
        for v in range(m):
            up[v] = v
            down[v] = m - 1 - v

        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for v in range(m):
                # previous value < current value
                new_up[v] = pref_down[v]

                # previous value > current value
                new_down[v] = (total_up - pref_up[v + 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD