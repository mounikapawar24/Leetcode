class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        from typing import List
        ans = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                # Land -> Water
                finish_land = ls + ld
                ans = min(ans, max(finish_land, ws) + wd)

                # Water -> Land
                finish_water = ws + wd
                ans = min(ans, max(finish_water, ls) + ld)

        return ans