from typing import List
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        n = len(positions)

        # keep original index
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])

        # sort by position (important for collision order)
        robots.sort(key=lambda x: x[0])

        stack = []   # robots moving right (indices in robots list)

        for i in range(n):
            pos, health, direction, idx = robots[i]

            if direction == 'R':
                stack.append(i)
            else:
                # direction == 'L' → may collide with previous 'R'
                while stack and robots[i][1] > 0:
                    j = stack[-1]  # last right-moving robot

                    # both alive → collide
                    if robots[j][1] < robots[i][1]:
                        # right robot dies
                        robots[i][1] -= 1
                        robots[j][1] = 0
                        stack.pop()

                    elif robots[j][1] > robots[i][1]:
                        # left robot dies
                        robots[j][1] -= 1
                        robots[i][1] = 0
                        break
                    else:
                        # equal health → both die
                        robots[j][1] = 0
                        robots[i][1] = 0
                        stack.pop()
                        break

        # collect survivors in original order
        survivors = []
        for pos, health, direction, idx in robots:
            if health > 0:
                survivors.append((idx, health))

        survivors.sort()  # restore input order
        return [h for _, h in survivors]