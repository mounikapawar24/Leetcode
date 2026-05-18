class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import defaultdict, deque
        n = len(arr)
        
        if n == 1:
            return 0
        
        # Store indices for each value
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        # BFS
        q = deque([(0, 0)])  # (index, steps)
        visited = set([0])
        
        while q:
            i, steps = q.popleft()
            
            # Reached last index
            if i == n - 1:
                return steps
            
            # Possible next jumps
            neighbors = []
            
            # Same value indices
            neighbors.extend(graph[arr[i]])
            
            # Adjacent indices
            if i + 1 < n:
                neighbors.append(i + 1)
            if i - 1 >= 0:
                neighbors.append(i - 1)
            
            for nei in neighbors:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, steps + 1))
            
            # Clear list to avoid repeated processing
            graph[arr[i]].clear()
        
        return -1