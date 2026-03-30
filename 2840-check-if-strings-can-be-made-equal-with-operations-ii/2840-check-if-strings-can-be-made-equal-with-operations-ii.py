class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        # compare characters at even indices (0, 2)
        if sorted(s1[::2]) != sorted(s2[::2]):
            return False
        
        # compare characters at odd indices (1, 3)
        if sorted(s1[1::2]) != sorted(s2[1::2]):
            return False
        
        return True