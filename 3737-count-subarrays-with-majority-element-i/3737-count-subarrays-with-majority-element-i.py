class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            cnt_target = 0
            length = 0

            for j in range(i, n):
                length += 1

                if nums[j] == target:
                    cnt_target += 1

                if cnt_target * 2 > length:
                    ans += 1

        return ans