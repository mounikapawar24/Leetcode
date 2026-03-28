class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # ---------- Step 1: basic diagonal validation ----------
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # ---------- Step 2: Union Find ----------
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        # merge indices that must be equal
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)

        # ---------- Step 3: assign smallest lexicographic letters ----------
        group_char = {}
        next_char = 0
        word = [''] * n

        for i in range(n):
            root = find(i)
            if root not in group_char:
                if next_char >= 26:
                    return ""   # only lowercase letters allowed
                group_char[root] = chr(ord('a') + next_char)
                next_char += 1
            word[i] = group_char[root]

        word = "".join(word)

        # ---------- Step 4: recompute LCP and verify ----------
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 0

                if dp[i][j] != lcp[i][j]:
                    return ""

        return word