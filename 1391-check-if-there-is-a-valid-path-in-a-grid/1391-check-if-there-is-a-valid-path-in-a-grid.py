class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        from collections import deque
        m, n = len(grid), len(grid[0])
        
        # Directions: (dx, dy)
        directions = {
            1: [(0, -1), (0, 1)],      # left, right
            2: [(-1, 0), (1, 0)],      # up, down
            3: [(0, -1), (1, 0)],      # left, down
            4: [(0, 1), (1, 0)],       # right, down
            5: [(0, -1), (-1, 0)],     # left, up
            6: [(0, 1), (-1, 0)]       # right, up
        }
        
        # Opposite direction mapping
        opposite = {
            (0, -1): (0, 1),
            (0, 1): (0, -1),
            (-1, 0): (1, 0),
            (1, 0): (-1, 0)
        }
        
        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        
        while queue:
            x, y = queue.popleft()
            
            # Reached destination
            if (x, y) == (m - 1, n - 1):
                return True
            
            # Explore valid directions from current cell
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    # Check if neighbor connects back
                    if opposite[(dx, dy)] in directions[grid[nx][ny]]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        
        return False