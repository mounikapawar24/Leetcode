class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # Replace each element with digit sum and return minimum
        return min(digit_sum(x) for x in nums)