class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height

        # directions in counter-clockwise order
        # East → North → West → South
        self.dirs = ["East", "North", "West", "South"]
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.dir_idx = 0      # start facing East
        self.x = 0
        self.y = 0

        # perimeter length (robot always walks along border)
        self.perim = 2 * (self.w + self.h) - 4

    def step(self, num: int) -> None:
        # movement repeats every perimeter cycle
        num %= self.perim

        # special rule:
        # if we are at (0,0) and complete a full cycle,
        # direction becomes South
        if num == 0 and (self.x, self.y) == (0, 0):
            self.dir_idx = 3  # South
            return

        while num > 0:
            dx, dy = self.moves[self.dir_idx]
            nx, ny = self.x + dx, self.y + dy

            # if next cell is outside → turn CCW
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir_idx = (self.dir_idx + 1) % 4
                continue

            # move one step
            self.x, self.y = nx, ny
            num -= 1

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.dirs[self.dir_idx]