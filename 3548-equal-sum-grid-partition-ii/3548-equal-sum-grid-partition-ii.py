from collections import Counter
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        # -------------------------------------------------
        # Check if we can remove one cell safely
        # -------------------------------------------------
        def can_remove(counter, diff, r1, r2, c1, c2):
            """
            section = rows [r1..r2], cols [c1..c2]
            check if removing value=diff keeps connectivity
            """

            if counter[diff] <= 0:
                return False

            rows = r2 - r1 + 1
            cols = c2 - c1 + 1

            # rectangle >= 2x2 → always connected after removal
            if rows > 1 and cols > 1:
                return True

            # single row → only endpoints allowed
            if rows == 1:
                if grid[r1][c1] == diff or grid[r1][c2] == diff:
                    return True
                return False

            # single column → only endpoints allowed
            if cols == 1:
                if grid[r1][c1] == diff or grid[r2][c1] == diff:
                    return True
                return False

            return False

        # =================================================
        # Horizontal cuts
        # =================================================
        top_sum = 0
        top_cnt = Counter()
        bottom_cnt = Counter(v for row in grid for v in row)

        for r in range(m - 1):
            for c in range(n):
                v = grid[r][c]
                top_sum += v
                top_cnt[v] += 1
                bottom_cnt[v] -= 1

            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # remove from larger section
            if top_sum > bottom_sum:
                if can_remove(top_cnt, diff, 0, r, 0, n - 1):
                    return True
            else:
                if can_remove(bottom_cnt, diff, r + 1, m - 1, 0, n - 1):
                    return True

        # =================================================
        # Vertical cuts
        # =================================================
        left_sum = 0
        left_cnt = Counter()
        right_cnt = Counter(v for row in grid for v in row)

        for c in range(n - 1):
            for r in range(m):
                v = grid[r][c]
                left_sum += v
                left_cnt[v] += 1
                right_cnt[v] -= 1

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if can_remove(left_cnt, diff, 0, m - 1, 0, c):
                    return True
            else:
                if can_remove(right_cnt, diff, 0, m - 1, c + 1, n - 1):
                    return True

        return False