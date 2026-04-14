class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        from functools import lru_cache
        robot.sort()
        factory.sort()
        
        n = len(robot)
        m = len(factory)
        
        @lru_cache(None)
        def dp(i, j):
            # If all robots are fixed
            if i == n:
                return 0
            
            # If no factories left but robots remain
            if j == m:
                return float('inf')
            
            res = float('inf')
            
            pos, limit = factory[j]
            
            # Option 1: skip this factory
            res = dp(i, j + 1)
            
            # Option 2: assign k robots to this factory
            dist = 0
            for k in range(1, limit + 1):
                if i + k > n:
                    break
                
                # add distance for kth robot
                dist += abs(robot[i + k - 1] - pos)
                
                res = min(res, dist + dp(i + k, j + 1))
            
            return res
        
        return dp(0, 0)