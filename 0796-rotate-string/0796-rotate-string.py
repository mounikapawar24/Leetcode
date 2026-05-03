class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Lengths must match
        if len(s) != len(goal):
            return False
        
        # Check if goal is substring of s+s
        return goal in (s + s)