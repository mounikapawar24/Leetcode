class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        res = [0] * n
        
        # Step 1: group indices by value
        mp = defaultdict(list)
        for i, val in enumerate(nums):
            mp[val].append(i)
        
        # Step 2: process each group
        for indices in mp.values():
            prefix = [0] * (len(indices) + 1)
            
            # build prefix sum
            for i in range(len(indices)):
                prefix[i + 1] = prefix[i] + indices[i]
            
            # calculate distances
            for i in range(len(indices)):
                idx = indices[i]
                
                # left contribution
                left = idx * i - prefix[i]
                
                # right contribution
                right = (prefix[len(indices)] - prefix[i + 1]) - idx * (len(indices) - i - 1)
                
                res[idx] = left + right
        
        return res