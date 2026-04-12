class Solution:
    def minimumDistance(self, word: str) -> int:
        # Convert letter to (row, col)
        def get_pos(c):
            idx = ord(c) - ord('A')
            return (idx // 6, idx % 6)
        
        # Manhattan distance
        def dist(a, b):
            if a is None:
                return 0
            x1, y1 = get_pos(a)
            x2, y2 = get_pos(b)
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(word)
        
        # dp[j] = max saving when second finger is at j
        dp = [0] * 26
        
        total = 0
        
        for i in range(1, n):
            cur = ord(word[i]) - ord('A')
            prev = ord(word[i - 1]) - ord('A')
            
            d = dist(word[i - 1], word[i])
            total += d
            
            new_dp = dp[:]
            
            for j in range(26):
                # Move second finger from j → current char
                saving = dp[j] + d - dist(chr(j + ord('A')), word[i])
                new_dp[prev] = max(new_dp[prev], saving)
            
            dp = new_dp
        
        return total - max(dp)