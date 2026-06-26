class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Transform:
        # target -> +1
        # others -> -1
        pref = [0]
        s = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            pref.append(s)

        vals = sorted(set(pref))
        comp = {v: i + 1 for i, v in enumerate(vals)}

        bit = [0] * (len(vals) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for p in pref:
            idx = comp[p]
            ans += query(idx - 1)
            update(idx)

        return ans