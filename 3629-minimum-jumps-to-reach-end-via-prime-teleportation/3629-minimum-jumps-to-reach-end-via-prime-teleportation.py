from collections import deque, defaultdict
from math import isqrt
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        MAXV = max(nums)

        # Smallest Prime Factor sieve
        spf = list(range(MAXV + 1))
        for i in range(2, isqrt(MAXV) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x >= 2 and spf[x] == x

        # Map: prime factor -> indices having numbers divisible by it
        div_map = defaultdict(list)

        for idx, val in enumerate(nums):
            x = val
            factors = set()

            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p

            for p in factors:
                div_map[p].append(idx)

        # BFS
        q = deque([0])
        dist = [-1] * n
        dist[0] = 0

        used_prime = set()

        while q:
            i = q.popleft()

            if i == n - 1:
                return dist[i]

            # Adjacent moves
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = dist[i] + 1
                    q.append(ni)

            # Prime teleportation
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                for ni in div_map[val]:
                    if dist[ni] == -1:
                        dist[ni] = dist[i] + 1
                        q.append(ni)

                used_prime.add(val)

        return -1