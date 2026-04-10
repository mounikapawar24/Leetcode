from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = float('inf')
        
        for v in pos:
            idx = pos[v]
            if len(idx) >= 3:
                for i in range(len(idx) - 2):
                    a = idx[i]
                    c = idx[i + 2]
                    ans = min(ans, 2 * (c - a))
        
        return ans if ans != float('inf') else -1