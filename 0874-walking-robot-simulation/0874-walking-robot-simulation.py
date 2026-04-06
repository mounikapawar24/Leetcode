class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
       
        obstacle_set = set(map(tuple, obstacles))

        # directions: North, East, South, West
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # start facing north

        x = y = 0
        max_dist = 0

        for cmd in commands:
            if cmd == -2:          # turn left
                d = (d - 1) % 4
            elif cmd == -1:        # turn right
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]

                # move one step at a time
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy

                    # stop if obstacle encountered
                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist