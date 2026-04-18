class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Reverse the number
        rev = int(str(n)[::-1])
        
        # Return absolute difference
        return abs(n - rev)