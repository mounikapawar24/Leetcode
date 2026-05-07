class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        from typing import List
        n = len(nums)

        # suffix_min[i] = minimum value from i to n-1
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        ans = [0] * n

        start = 0
        prefix_max = nums[0]

        for i in range(n - 1):
            prefix_max = max(prefix_max, nums[i])

            # Split components when:
            # every value on left <= every value on right
            if prefix_max <= suffix_min[i + 1]:

                comp_max = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = comp_max

                start = i + 1
                prefix_max = nums[start]

        # Last component
        comp_max = max(nums[start:])

        for j in range(start, n):
            ans[j] = comp_max

        return ans