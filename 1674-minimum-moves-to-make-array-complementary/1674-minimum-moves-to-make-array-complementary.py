class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        # Difference array
        diff = [0] * (2 * limit + 2)

        left, right = 0, n - 1

        while left < right:
            a = nums[left]
            b = nums[right]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # Default cost = 2
            diff[2] += 2

            # Cost becomes 1 in [low, high]
            diff[low] -= 1
            diff[high + 1] += 1

            # Cost becomes 0 at exact sum s
            diff[s] -= 1
            diff[s + 1] += 1

            left += 1
            right -= 1

        ans = float('inf')
        curr = 0

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans