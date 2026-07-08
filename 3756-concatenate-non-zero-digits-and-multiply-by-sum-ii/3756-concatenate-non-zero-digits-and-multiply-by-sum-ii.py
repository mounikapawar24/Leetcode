class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Prefix count of non-zero digits
        cnt = [0] * (n + 1)

        # Prefix sum of non-zero digits
        sm = [0] * (n + 1)

        # Prefix value:
        # val[i] = number formed by all non-zero digits in s[:i]
        val = [0] * (n + 1)

        # inv10[k] = inverse of 10^k
        pow10 = [1] * (n + 1)
        inv10 = [1] * (n + 1)
        inv10_base = pow(10, MOD - 2, MOD)

        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD
            inv10[i] = inv10[i - 1] * inv10_base % MOD

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            cnt[i + 1] = cnt[i]
            sm[i + 1] = sm[i]
            val[i + 1] = val[i]
            if d:
                cnt[i + 1] += 1
                sm[i + 1] += d
                val[i + 1] = (val[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            k = cnt[r + 1] - cnt[l]
            digit_sum = sm[r + 1] - sm[l]

            if k == 0:
                ans.append(0)
                continue

            x = (val[r + 1] - val[l] * pow10[k]) % MOD
            ans.append(x * digit_sum % MOD)

        return ans