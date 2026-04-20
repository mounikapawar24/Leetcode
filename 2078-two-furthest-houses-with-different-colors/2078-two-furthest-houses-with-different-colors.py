class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        ans=0
        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                  ans=max(ans,i-0)
                  break
        for i in range(n):
            if colors[i]!=colors[n-1]:
                ans=max(ans,(n-1)-i)
                break
        return ans