from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        ans = []

        for x in nums:
            right = total - left - x
            ans.append(abs(left - right))
            left += x

        return ans