from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # total sum of grid
        total = sum(sum(row) for row in grid)

        # If total is odd → impossible
        if total % 2 != 0:
            return False

        target = total // 2

        # ---------- Check horizontal cut ----------
        running = 0
        for i in range(m - 1):          # cut must leave bottom non-empty
            running += sum(grid[i])
            if running == target:
                return True

        # ---------- Check vertical cut ----------
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]

        running = 0
        for j in range(n - 1):          # cut must leave right non-empty
            running += col_sums[j]
            if running == target:
                return True

        return False