class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse_num(x):
            rev = 0
            while x > 0:
                rev = rev * 10 + x % 10
                x //= 10
            return rev
        
        last_seen = {}  # stores reverse(nums[i]) -> index i
        ans = float('inf')
        
        for j, num in enumerate(nums):
            # check if current matches any previous reversed value
            if num in last_seen:
                ans = min(ans, j - last_seen[num])
            
            # store reverse of current for future matches
            rev = reverse_num(num)
            last_seen[rev] = j
        
        return ans if ans != float('inf') else -1